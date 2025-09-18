# 🧠 Memory Agent

A sophisticated AI-powered memory agent that combines FastAPI backend with Streamlit frontend, featuring persistent memory storage using ChromaDB and Redis for conversation history.

## ✨ Features

- **Persistent Memory**: Long-term memory storage using ChromaDB vector database
- **Conversation History**: Session-based chat history with Redis
- **Modern UI**: Clean Streamlit interface for easy interaction
- **RESTful API**: FastAPI backend with automatic documentation
- **Docker Ready**: Complete containerization with Docker Compose
- **Scalable**: Microservices architecture for easy scaling

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Streamlit     │    │   FastAPI       │    │     Redis       │
│   Frontend      │◄──►│   Backend       │◄──►│   (Sessions)    │
│   (Port 8501)   │    │   (Port 8000)   │    │   (Port 6379)   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │    ChromaDB     │
                       │  (Vector Store) │
                       └─────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- Docker and Docker Compose
- OpenAI API Key

### 1. Clone the Repository

```bash
git clone https://github.com/Hezekiahpilli/memory-agent.git
cd memory-agent
```

### 2. Set Up Environment Variables

Create a `.env` file in the `backend/` directory:

```bash
# OpenAI API Key (required)
OPENAI_API_KEY=your_openai_api_key_here

# Redis Configuration
REDIS_URL=redis://redis:6379/0

# ChromaDB Configuration
CHROMA_DIR=/data/chroma

# CORS Configuration
ALLOWED_ORIGINS=http://localhost:8501,http://127.0.0.1:8501
```

### 3. Run with Docker Compose

```bash
docker-compose up --build
```

### 4. Access the Application

- **Frontend**: http://localhost:8501
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## 📁 Project Structure

```
memory-agent/
├── backend/
│   ├── app.py              # FastAPI application
│   ├── agent.py            # AI agent logic
│   ├── memory.py           # Memory management
│   ├── models.py           # Pydantic models
│   ├── requirements.txt    # Python dependencies
│   ├── Dockerfile          # Backend container
│   └── .env               # Environment variables
├── frontend/
│   ├── streamlit_app.py    # Streamlit interface
│   ├── requirements.txt    # Frontend dependencies
│   └── Dockerfile          # Frontend container
├── data/
│   └── chroma/            # ChromaDB data directory
├── docker-compose.yml     # Multi-container setup
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## 🔧 API Endpoints

### Chat with Memory
```http
POST /api/chat
Content-Type: application/json

{
  "session_id": "unique-session-id",
  "message": "Your message here"
}
```

### Clear Session History
```http
POST /api/clear
Content-Type: application/json

{
  "session_id": "unique-session-id"
}
```

## 🛠️ Development

### Running Locally (without Docker)

1. **Backend Setup**:
```bash
cd backend
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 8000
```

2. **Frontend Setup**:
```bash
cd frontend
pip install -r requirements.txt
streamlit run streamlit_app.py --server.port 8501
```

3. **Redis Setup**:
```bash
docker run -d -p 6379:6379 redis:7-alpine
```

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `OPENAI_API_KEY` | OpenAI API key for LLM | Required |
| `REDIS_URL` | Redis connection URL | `redis://redis:6379/0` |
| `CHROMA_DIR` | ChromaDB data directory | `/data/chroma` |
| `ALLOWED_ORIGINS` | CORS allowed origins | `http://localhost:8501` |
| `OPENAI_MODEL` | OpenAI model to use | `gpt-4o-mini` |

## 🧠 How Memory Works

1. **Short-term Memory**: Redis stores conversation history per session
2. **Long-term Memory**: ChromaDB stores vectorized memories for retrieval
3. **Context Building**: Agent retrieves relevant memories and recent history
4. **Memory Updates**: New conversations are automatically stored as memories

## 🐳 Docker Services

- **backend**: FastAPI application with AI agent
- **frontend**: Streamlit web interface
- **redis**: Session storage and caching
- **chroma**: Vector database for long-term memory

## 📝 Usage Examples

### Basic Chat
1. Open http://localhost:8501
2. Type your message
3. Click "Send"
4. The agent will respond using its memory

### API Usage
```python
import requests

# Chat with the agent
response = requests.post("http://localhost:8000/api/chat", json={
    "session_id": "user123",
    "message": "Hello, remember my name is John"
})

# Clear session
requests.post("http://localhost:8000/api/clear", json={
    "session_id": "user123"
})
```

## 🔒 Security Notes

- Store your OpenAI API key securely
- Use environment variables for sensitive data
- Consider using HTTPS in production
- Implement proper authentication for production use

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Troubleshooting

### Common Issues

1. **Backend not starting**: Check if OpenAI API key is set
2. **Memory not persisting**: Ensure ChromaDB directory has write permissions
3. **CORS errors**: Verify ALLOWED_ORIGINS includes your frontend URL
4. **Redis connection issues**: Check if Redis container is running

### Logs

```bash
# View all logs
docker-compose logs

# View specific service logs
docker-compose logs backend
docker-compose logs frontend
```

## 🚀 Deployment

### Production Considerations

- Use a production WSGI server (e.g., Gunicorn)
- Set up proper logging
- Configure reverse proxy (Nginx)
- Use managed Redis and database services
- Implement monitoring and health checks

---

**Made with ❤️ by Hezekiahpilli**
