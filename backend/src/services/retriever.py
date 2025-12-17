from typing import List, Dict, Any
import logging
from qdrant_client import QdrantClient
from qdrant_client.http import models
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from src.core.config import settings
import openai

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Retriever:
    def __init__(self):
        # Initialize Qdrant client
        self.qdrant_client = QdrantClient(
            url=settings.QDRANT_URL,
            api_key=settings.QDRANT_API_KEY,
            prefer_grpc=False
        )
        self.collection_name = settings.QDRANT_COLLECTION_NAME
        
        # Initialize Neon Postgres connection
        if settings.NEON_DATABASE_URL:
            self.db_engine = create_engine(settings.NEON_DATABASE_URL)
            self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.db_engine)
        else:
            self.db_engine = None
            self.SessionLocal = None

    async def retrieve(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        """
        Retrieve relevant documents based on the query
        """
        try:
            logger.info(f"Starting retrieval for query: {query}")
            
            # Step 1: Generate embeddings for the query
            logger.info("Step 1: Generating embeddings for query")
            query_embedding = await self._get_embedding(query)
            logger.info(f"Generated embedding with {len(query_embedding)} dimensions")
            
            # Step 2: Search in Qdrant for similar documents
            logger.info(f"Step 2: Searching in Qdrant collection: {self.collection_name}")
            search_results = self.qdrant_client.search(
                collection_name=self.collection_name,
                query_vector=query_embedding,
                limit=top_k
            )
            
            logger.info(f"Found {len(search_results)} results from Qdrant")
            
            # Step 3: Retrieve document content from Neon Postgres using IDs from Qdrant
            logger.info("Step 3: Retrieving document content from Neon Postgres")
            documents = []
            doc_ids = [result.id for result in search_results]
            
            if doc_ids and self.db_engine:
                documents = await self._get_documents_by_ids(doc_ids)
            elif doc_ids:
                # If no database connection, return metadata from Qdrant
                for result in search_results:
                    doc = {
                        "id": result.id,
                        "content": result.payload.get("content", ""),
                        "source": result.payload.get("source", ""),
                        "score": result.score
                    }
                    documents.append(doc)
            else:
                logger.warning("No documents found in Qdrant")
            
            logger.info(f"Retrieved {len(documents)} documents with content")
            return documents
            
        except Exception as e:
            logger.error(f"Error during retrieval: {str(e)}")
            raise

    async def _get_embedding(self, text: str) -> List[float]:
        """
        Generate embedding for the given text using OpenAI
        """
        try:
            openai.api_key = settings.OPENAI_API_KEY
            
            response = openai.Embedding.create(
                input=text,
                model="text-embedding-ada-002"
            )
            
            embedding = response['data'][0]['embedding']
            logger.info(f"Generated embedding with {len(embedding)} dimensions")
            return embedding
        except Exception as e:
            logger.error(f"Error generating embedding: {str(e)}")
            raise

    async def _get_documents_by_ids(self, doc_ids: List[str]) -> List[Dict[str, Any]]:
        """
        Retrieve document content from Neon Postgres by IDs
        """
        if not self.db_engine:
            logger.warning("No database connection available")
            return []
        
        try:
            with self.SessionLocal() as db:
                # Create a placeholder query for the IDs
                id_placeholders = ','.join([f"'{doc_id}'" for doc_id in doc_ids])
                
                query = text(f"""
                    SELECT id, content, source, metadata 
                    FROM documents 
                    WHERE id IN ({id_placeholders})
                """)
                
                result = db.execute(query)
                rows = result.fetchall()
                
                documents = []
                for row in rows:
                    doc = {
                        "id": row[0],
                        "content": row[1],
                        "source": row[2],
                        "metadata": row[3]
                    }
                    documents.append(doc)
                
                logger.info(f"Fetched {len(documents)} documents from database")
                return documents
                
        except Exception as e:
            logger.error(f"Error fetching documents from database: {str(e)}")
            # Return an empty list if there's an error
            return []