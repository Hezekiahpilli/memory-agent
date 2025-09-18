import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from models import ChatRequest, ChatResponse, ClearRequest, Source
from agent import chat
from memory import clear_history

load_dotenv()
app = FastAPI()
origins = [o for o in os.getenv("ALLOWED_ORIGINS","http://localhost:8501").split(",") if o]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.post("/api/chat", response_model=ChatResponse)
def api_chat(req: ChatRequest):
    reply, mems = chat(req.session_id, req.message)
    sources = [Source(doc_id=f"memory_{i+1}", score=float(s), text=t[:240]) for i,(t,s) in enumerate(mems)]
    return ChatResponse(reply=reply, sources=sources)

@app.post("/api/clear")
def api_clear(req: ClearRequest):
    clear_history(req.session_id)
    return {"ok": True}
