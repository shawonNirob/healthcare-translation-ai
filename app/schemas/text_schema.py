from pydantic import BaseModel

class AskRequest(BaseModel):
    query: str 
    preferred_language: str 