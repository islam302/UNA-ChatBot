import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')  # Ensure this is set

def test_chatgpt_response():
    prompt = "??? ???? ????"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        print(response.choices[0].message['content'].strip())
    except Exception as e:
        print(f"Error: {e}")

test_chatgpt_response()
