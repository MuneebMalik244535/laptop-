import os
import asyncpg
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

async def get_neon_connection():
    """
    Returns a connection to Neon Postgres database
    """
    neon_postgres_url = os.getenv("NEON_POSTGRES_URL")
    
    if not neon_postgres_url:
        raise ValueError("NEON_POSTGRES_URL environment variable is required")
    
    # Extract connection parameters from the URL
    # The URL format is typically: postgresql://username:password@ep-xxx.us-east-1.aws.neon.tech/dbname?sslmode=require
    conn = await asyncpg.connect(dsn=neon_postgres_url)
    
    return conn

async def get_pool():
    """
    Returns a connection pool for Neon Postgres database
    """
    neon_postgres_url = os.getenv("NEON_POSTGRES_URL")
    
    if not neon_postgres_url:
        raise ValueError("NEON_POSTGRES_URL environment variable is required")
    
    pool = await asyncpg.create_pool(dsn=neon_postgres_url)
    
    return pool