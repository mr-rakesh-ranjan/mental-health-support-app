from pydantic import BaseModel

# models
class UserInput(BaseModel):
    user_query: str
    feelings: str | None = None
    history: str | None = None

class CopingInput(BaseModel):
    category :str
    subcategory: str

class ConversationData(BaseModel):
    conversation_data: list