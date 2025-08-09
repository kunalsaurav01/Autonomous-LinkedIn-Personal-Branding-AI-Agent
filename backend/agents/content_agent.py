from openai import OpenAI
from models.schemas import UserProfile

def generate_post(profile: UserProfile):
    prompt = f"Create a LinkedIn post for a {profile.role} in {profile.industry} interested in {', '.join(profile.interests)}."
    response = OpenAI().ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return {"post": response['choices'][0]['message']['content']}
