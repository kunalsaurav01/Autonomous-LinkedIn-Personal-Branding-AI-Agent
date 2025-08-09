from fastapi import FastAPI
from agents.content_agent import generate_post
from models.schemas import UserProfile
from services.linkedin_api import post_to_linkedin

app = FastAPI()

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class PostRequest(BaseModel):
    name: str
    role: str
    industry: str
    interests: List[str]

@app.post("/generate")
def generate_post(data: PostRequest):
    interests_str = ", ".join(data.interests)
    post = (
        f"🚀 Meet {data.name}, a passionate {data.role} in the {data.industry} industry.\n"
        f"🔍 Exploring cutting-edge topics like {interests_str}.\n"
        f"💡 Always pushing boundaries with innovation and curiosity!"
    )
    return {"post": post}


@app.get("/")
def read_root():
    return {"message": "LinkedIn AI Agent is running!"}


# @app.post("/generate")
# def create_content(profile: UserProfile):
#     return generate_post(profile)

@app.post("/post")
def publish_content(profile: UserProfile):
    content = generate_post(profile)
    response = post_to_linkedin(content)
    return {"status": "posted", "response": response}
