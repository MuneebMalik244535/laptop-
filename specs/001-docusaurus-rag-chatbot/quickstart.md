# Quickstart: Docusaurus RAG Chatbot Integration

## Getting Started

Follow these steps to begin implementing the Docusaurus RAG Chatbot Integration feature.

### 1. Set Up Development Environment

#### Backend Setup
```bash
# Install Python dependencies
cd backend
pip install -r requirements.txt
```

#### Frontend Setup
```bash
# Install Node.js dependencies
cd frontend
npm install
```

### 2. Configure Environment Variables

Create `.env` files in both backend and frontend directories:

**backend/.env**
```env
QDRANT_URL=your-qdrant-cloud-url
QDRANT_API_KEY=your-qdrant-api-key
NEON_POSTGRES_URL=your-neon-postgres-url
OPENAI_API_KEY=your-openai-api-key
```

**frontend/.env**
```env
REACT_APP_BACKEND_URL=http://localhost:8000
```

### 3. Start Development Servers

#### Start Backend
```bash
# In backend directory
cd backend
python main.py
```

#### Start Frontend
```bash
# In frontend directory
cd frontend
npm start
```

### 4. Verify API Endpoints

Test the backend API endpoints:

```bash
# Test health endpoint
curl http://localhost:8000/health

# Test query endpoint (replace with your question)
curl -X POST http://localhost:8000/query -H "Content-Type: application/json" -d '{"question": "What is the main topic of this book?", "selected_text": ""}'
```

### 5. Implementation Phases

The implementation will proceed through the following phases:

**Phase 1: Docusaurus Floating Button + Popup Component Setup**
- Create React component for floating button
- Implement animation and positioning
- Add portal for overlay functionality

**Phase 2: Chatbox React Component**
- Create chat interface component with message history
- Implement input field and send functionality
- Add loading states and error handling

**Phase 3: FastAPI Backend Skeleton**
- Set up basic FastAPI structure
- Implement /query, /select-text, and /health endpoints
- Add request validation

**Phase 4: Retrieval Pipeline**
- Connect to Qdrant Cloud for vector search
- Connect to Neon Postgres for metadata retrieval
- Implement context building and OpenAI integration

**Phase 5: Frontend-Backend Connection**
- Implement API service layer in frontend
- Connect chat component to backend endpoints
- Handle authentication and error states

**Phase 6: End-to-End Testing**
- Create test cases with sample questions
- Verify answers are based on book content
- Test edge cases and error scenarios

**Phase 7: Final Integration**
- Build static files for Docusaurus
- Ensure minimal CSS/JS impact
- Deploy to production environment

### 6. Next Steps

After completing the setup, begin with Phase 1 implementation by creating the floating button component.