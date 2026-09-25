import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_story(outline):
    model = genai.GenerativeModel("gemini-1.5-pro")
    prompt = "Expand this outline into narration and dialogues:\n"
    for panel in outline:
        prompt += f"{panel['title']}: {panel['desc']}\n"
    response = model.generate_content(prompt)
    return response.text
