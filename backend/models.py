from pydantic import BaseModel
from typing import Optional
# models
class UserInput(BaseModel):
    user_query: str
    feelings: Optional[str] = None
    history: Optional[list] = None

class CopingInput(BaseModel):
    category :str
    subcategory: str

class ConversationData(BaseModel):
    conversation_data: list