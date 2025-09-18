import os, json
from typing import List, Tuple
from langchain_openai import OpenAIEmbeddings
from langchain.schema import Document
from langchain.vectorstores import Chroma
from redis import Redis

CHROMA_DIR = os.getenv("CHROMA_DIR","./.chroma")

def get_vectorstore():
    embeddings = OpenAIEmbeddings()
    return Chroma(collection_name="long_term_memory", embedding_function=embeddings, persist_directory=CHROMA_DIR)

def upsert_memories(pairs: List[Tuple[str,str]]):
    vs = get_vectorstore()
    docs = [Document(page_content=c, metadata={"role": r}) for r,c in pairs if c.strip()]
    if docs:
        vs.add_documents(docs)
        vs.persist()

def search_memories(q: str, k: int=4):
    vs = get_vectorstore()
    return [(doc.page_content, float(score)) for doc, score in vs.similarity_search_with_score(q, k=k)]

def get_redis():
    url = os.getenv("REDIS_URL","")
    return Redis.from_url(url, decode_responses=True) if url else None

def append_history(session_id: str, role: str, content: str):
    r = get_redis()
    if r:
        import json as _j
        r.rpush(f"chat:{session_id}", _j.dumps({"role": role, "content": content}))

def read_history(session_id: str):
    r = get_redis()
    items = []
    if r:
        import json as _j
        for raw in r.lrange(f"chat:{session_id}", 0, -1):
            o = _j.loads(raw); items.append((o.get("role","user"), o.get("content","")))
    return items

def clear_history(session_id: str):
    r = get_redis()
    if r: r.delete(f"chat:{session_id}")
