from pydantic import BaseModel, Field
from typing import List

class ChatRequest(BaseModel):
    session_id: str
    message: str

class Source(BaseModel):
    doc_id: str
    score: float
    text: str

class ChatResponse(BaseModel):
    reply: str
    sources: List[Source] = []

class ClearRequest(BaseModel):
    session_id: str
