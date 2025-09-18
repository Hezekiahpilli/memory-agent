import os
from typing import Tuple
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from memory import search_memories, upsert_memories, read_history, append_history

SYSTEM = "You are a helpful assistant with memory."

def build_context(session_id: str, user_msg: str):
    memories = search_memories(user_msg, k=4)
    history_pairs = read_history(session_id)[-12:]
    msgs = [SystemMessage(content=SYSTEM)]
    for role, content in history_pairs:
        msgs.append(HumanMessage(content=content) if role=="user" else AIMessage(content=content))
    msgs.append(HumanMessage(content=user_msg))
    return msgs, memories

def chat(session_id: str, user_msg: str):
    llm = ChatOpenAI(model=os.getenv("OPENAI_MODEL","gpt-4o-mini"), temperature=0.2)
    msgs, mems = build_context(session_id, user_msg)
    resp = llm.invoke(msgs)
    reply = getattr(resp, "content", str(resp))
    append_history(session_id, "user", user_msg)
    append_history(session_id, "assistant", reply)
    upsert_memories([("user", user_msg), ("assistant", reply)])
    return reply, mems
