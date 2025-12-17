from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import logging

from src.services.rag_pipeline import RAGPipeline
from src.core.config import settings

router = APIRouter(prefix="/rag", tags=["rag"])

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class QueryRequest(BaseModel):
    query: str
    session_id: Optional[str] = None

class QueryResponse(BaseModel):
    response: str
    sources: Optional[List[str]] = None
    session_id: Optional[str] = None

class SelectTextRequest(BaseModel):
    text: str
    query: str
    session_id: Optional[str] = None

class HealthResponse(BaseModel):
    status: str
    version: str

@router.post("/query", response_model=QueryResponse)
async def query_endpoint(request: QueryRequest):
    """
    Process a user query using the RAG pipeline
    """
    try:
        logger.info(f"Processing query: {request.query}")
        
        # Initialize the RAG pipeline
        rag_pipeline = RAGPipeline()
        
        # Get the response from the RAG pipeline
        response = await rag_pipeline.process_query(request.query)
        
        logger.info(f"Response generated successfully")
        
        return QueryResponse(
            response=response.answer,
            sources=response.sources,
            session_id=request.session_id
        )
    except Exception as e:
        logger.error(f"Error processing query: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")

@router.post("/select-text", response_model=QueryResponse)
async def select_text_endpoint(request: SelectTextRequest):
    """
    Process a query with selected text context
    """
    try:
        logger.info(f"Processing query with selected text: {request.query}")
        
        # Initialize the RAG pipeline
        rag_pipeline = RAGPipeline()
        
        # Process the query with the selected text context
        response = await rag_pipeline.process_query_with_context(request.query, request.text)
        
        logger.info(f"Response with context generated successfully")
        
        return QueryResponse(
            response=response.answer,
            sources=response.sources,
            session_id=request.session_id
        )
    except Exception as e:
        logger.error(f"Error processing query with context: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing query with context: {str(e)}")

@router.get("/health", response_model=HealthResponse)
async def health_check():
    """
    Health check endpoint for the RAG service
    """
    try:
        logger.info("Health check requested")
        
        # Add any additional health checks here
        # For example, check if Qdrant and Neon connections are available
        
        return HealthResponse(
            status="healthy",
            version=settings.APP_VERSION
        )
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Health check failed: {str(e)}")