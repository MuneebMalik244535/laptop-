from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import uuid

Base = declarative_base()

def generate_uuid():
    return str(uuid.uuid4())

class ChatSession(Base):
    __tablename__ = "chat_sessions"
    
    id = Column(String, primary_key=True, index=True, default=generate_uuid)
    user_id = Column(String, nullable=False)
    start_time = Column(DateTime, server_default=func.now(), nullable=False)
    end_time = Column(DateTime)
    is_active = Column(Boolean, default=True, nullable=False)
    last_activity = Column(DateTime, server_default=func.now())

class UserQuery(Base):
    __tablename__ = "user_queries"
    
    id = Column(String, primary_key=True, index=True, default=generate_uuid)
    text = Column(Text, nullable=False)
    timestamp = Column(DateTime, server_default=func.now(), nullable=False)
    chat_session_id = Column(String, nullable=False)
    context = Column(Text)