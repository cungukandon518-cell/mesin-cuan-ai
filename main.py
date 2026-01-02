import os
from google import genai
from google.genai import types

def generate_blog_post(topic):
    # This is using Replit's AI Integrations service, which provides Gemini-compatible API access
    # without requiring your own Gemini API key.
    AI_INTEGRATIONS_GEMINI_API_KEY = os.environ.get("AI_INTEGRATIONS_GEMINI_API_KEY")
    AI_INTEGRATIONS_GEMINI_BASE_URL = os.environ.get("AI_INTEGRATIONS_GEMINI_BASE_URL")

    if not AI_INTEGRATIONS_GEMINI_API_KEY or not AI_INTEGRATIONS_GEMINI_BASE_URL:
        print("Error: Replit AI Integrations environment variables not found.")
        return

    client = genai.Client(
        api_key=AI_INTEGRATIONS_GEMINI_API_KEY,
        http_options={
            'api_version': '',
            'base_url': AI_INTEGRATIONS_GEMINI_BASE_URL   
        }
    )

    prompt = f"Write a comprehensive, engaging blog post in Markdown format about '{topic}'. Include a catchy title, headings, and a conclusion."
    
    print(f"Generating blog post for topic: {topic}...")
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        content = response.text

        if not content:
            print("Error: No content generated.")
            return

        with open('article.md', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Successfully saved blog post to 'article.md'")
    except Exception as e:
        print(f"An error occurred during generation: {e}")

if __name__ == "__main__":
    topic = input("Enter a topic for your blog post: ")
    if topic:
        generate_blog_post(topic)
    else:
        print("Topic cannot be empty.")
