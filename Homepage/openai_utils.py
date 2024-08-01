import requests

# Fetch API Key from environment variable
GPT4V_KEY = '17bd4c377c8248f3a08bacb8c30e79c6'

def get_chatgpt_response(user_question):
    payload = {
        "messages": [
            {
                "role": "system",
                "content": "??? ????? ??? ????? ????? ?? ?????? ??? ?????????. ??? ?? ???? ???? ?????? ?????? ???????."
            },
            {
                "role": "user",
                "content": user_question  # The question in Arabic
            }
        ],
        "temperature": 0.7,
        "top_p": 0.95,
        "max_tokens": 800
    }

    # Define the endpoint
    GPT4V_ENDPOINT = "https://islam.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-02-15-preview"

    # Define headers
    headers = {
        "Content-Type": "application/json",
        "api-key": GPT4V_KEY,
    }

    # Send request
    try:
        response = requests.post(GPT4V_ENDPOINT, headers=headers, json=payload)
        response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
    except requests.RequestException as e:
        raise SystemExit(f"Failed to make the request. Error: {e}")

    # Handle the response
    response_json = response.json()
    assistant_message = response_json['choices'][0]['message']['content']
    return assistant_message
