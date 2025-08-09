from pydantic import BaseModel

class UserProfile(BaseModel):
    name: str
    role: str
    industry: str
    interests: list[str]
