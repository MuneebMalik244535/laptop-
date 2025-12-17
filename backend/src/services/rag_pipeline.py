from typing import List, Optional
from pydantic import BaseModel
import logging
from src.services.retriever import Retriever
from src.services.openai_service import OpenAIService

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class QueryResponse(BaseModel):
    answer: str
    sources: Optional[List[str]] = None

class RAGPipeline:
    def __init__(self):
        self.retriever = Retriever()
        self.openai_service = OpenAIService()

    async def process_query(self, query: str) -> QueryResponse:
        """
        Process a user query using the RAG pipeline
        """
        try:
            logger.info(f"Starting RAG pipeline for query: {query}")
            
            # Step 1: Retrieve relevant documents
            logger.info("Step 1: Retrieving relevant documents")
            relevant_docs = await self.retriever.retrieve(query)
            logger.info(f"Retrieved {len(relevant_docs)} relevant documents")
            
            # Step 2: Build context from retrieved documents
            logger.info("Step 2: Building context from retrieved documents")
            context = self._build_context(relevant_docs)
            logger.info(f"Built context with {len(context)} characters")
            
            # Step 3: Generate response using OpenAI
            logger.info("Step 3: Generating response using OpenAI")
            answer = await self.openai_service.generate_response(query, context)
            logger.info("Response generated successfully")
            
            # Extract sources for attribution
            sources = [doc.get("source", "Unknown") for doc in relevant_docs]
            
            return QueryResponse(answer=answer, sources=sources)
            
        except Exception as e:
            logger.error(f"Error in RAG pipeline: {str(e)}")
            raise

    async def process_query_with_context(self, query: str, text_context: str) -> QueryResponse:
        """
        Process a query with additional text context
        """
        try:
            logger.info(f"Starting RAG pipeline with context for query: {query}")
            
            # Step 1: Retrieve relevant documents based on query
            logger.info("Step 1: Retrieving relevant documents")
            relevant_docs = await self.retriever.retrieve(query)
            logger.info(f"Retrieved {len(relevant_docs)} relevant documents")
            
            # Step 2: Build context from retrieved documents and provided text context
            logger.info("Step 2: Building context from retrieved documents and provided text")
            context = self._build_context(relevant_docs, text_context)
            logger.info(f"Built context with {len(context)} characters")
            
            # Step 3: Generate response using OpenAI
            logger.info("Step 3: Generating response using OpenAI")
            answer = await self.openai_service.generate_response(query, context)
            logger.info("Response generated successfully")
            
            # Extract sources for attribution
            sources = [doc.get("source", "Unknown") for doc in relevant_docs]
            sources.append("Selected Text")
            
            return QueryResponse(answer=answer, sources=sources)
            
        except Exception as e:
            logger.error(f"Error in RAG pipeline with context: {str(e)}")
            raise

    def _build_context(self, docs: List[dict], text_context: Optional[str] = None) -> str:
        """
        Build context string from retrieved documents and optional text context
        """
        context_parts = []
        
        # Add text context if provided
        if text_context:
            context_parts.append(f"Selected Text Context: {text_context}\n")
        
        # Add content from retrieved documents
        for doc in docs:
            content = doc.get("content", "")
            if content:
                context_parts.append(content)
        
        return "\n\n".join(context_parts)