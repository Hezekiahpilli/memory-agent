import os, requests, uuid
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
API_URL=os.getenv("API_URL","http://localhost:8000")
st.set_page_config(page_title="Memory Agent", page_icon="🧠")
st.title("🧠 Memory Agent")
if "sid" not in st.session_state:
    st.session_state.sid=str(uuid.uuid4())
msg=st.text_area("Message")
if st.button("Send"):
    r=requests.post(f"{API_URL}/api/chat", json={"session_id":st.session_state.sid, "message":msg})
    st.write(r.json())
