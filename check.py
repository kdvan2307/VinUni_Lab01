import os
from google import genai

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

models = [
    "gemini-3.8-flash",
    "gemini-3.5-flash",
    "gemini-3.1-flash-lite",
]

for model in models:
    print(f"\nTesting: {model}")

    try:
        response = client.models.generate_content(
            model=model,
            contents="Xin chào, hãy trả lời ngắn gọn."
        )

        print("SUCCESS:", response.text)
        print("Model hoạt động:", model)
        break

    except Exception as e:
        print("FAILED:", str(e)[:300])