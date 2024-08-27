from pydantic import BaseModel

# models
class UserInput(BaseModel):
    user_query: str
    feelings: str | None = None
    history: str | None = None