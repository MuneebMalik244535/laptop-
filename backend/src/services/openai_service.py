import openai
import logging
from src.core.config import settings

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class OpenAIService:
    def __init__(self):
        openai.api_key = settings.OPENAI_API_KEY
        self.model = settings.OPENAI_MODEL

    async def generate_response(self, query: str, context: str) -> str:
        """
        Generate a response using OpenAI based on the query and context
        """
        try:
            logger.info("Generating response using OpenAI")
            
            # Construct the prompt with context
            prompt = f"""
            You are an AI assistant helping users with questions about a book. 
            Use the following context to answer the question. 
            If the answer cannot be found in the context, say "I don't have enough information in the book to answer that question."
            
            Context:
            {context}
            
            Question: {query}
            
            Answer:
            """
            
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {
                        "role": "system", 
                        "content": "You are a helpful assistant that answers questions based on provided context. Only use information from the context provided."
                    },
                    {
                        "role": "user", 
                        "content": prompt
                    }
                ],
                max_tokens=1000,
                temperature=0.3
            )
            
            answer = response.choices[0].message['content'].strip()
            logger.info("Response generated successfully")
            
            return answer
        except Exception as e:
            logger.error(f"Error generating response: {str(e)}")
            raise