import os
from qdrant_client import QdrantClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_qdrant_client():
    """
    Returns a configured Qdrant client instance
    """
    qdrant_url = os.getenv("QDRANT_URL")
    qdrant_api_key = os.getenv("QDRANT_API_KEY")
    
    if not qdrant_url:
        raise ValueError("QDRANT_URL environment variable is required")
    
    if qdrant_api_key:
        client = QdrantClient(
            url=qdrant_url,
            api_key=qdrant_api_key,
            prefer_grpc=False  # Using REST API
        )
    else:
        # For local instance without authentication
        client = QdrantClient(
            url=qdrant_url
        )
    
    return client

# Create a global client instance
qdrant_client = get_qdrant_client()