# #
# # import os
# # import requests
# # import base64
# #
# # # Fetch API Key from environment variable
# # GPT4V_KEY = '17bd4c377c8248f3a08bacb8c30e79c6'
# # if not GPT4V_KEY:
# #     raise ValueError("API key is missing. Please set the environment variable GPT4V_API_KEY.")
# #
# # # Define image path and encode the image if needed
# # # IMAGE_PATH = "icon16ChatTk.ico"  # Replace with the actual image path
# # # if IMAGE_PATH:
# # #     try:
# # #         with open(IMAGE_PATH, 'rb') as image_file:
# # #             encoded_image = base64.b64encode(image_file.read()).decode('ascii')
# # #     except FileNotFoundError:
# # #         raise ValueError("Image file not found. Please check the path.")
# # # else:
# # #     encoded_image = None
# #
# # # Define headers
# # headers = {
# #     "Content-Type": "application/json",
# #     "api-key": GPT4V_KEY,
# # }
# #
# # # Define the payload for the request
# # payload = {
# #     "messages": [
# #         {
# #             "role": "system",
# #             "content": [
# #                 {
# #                     "type": "text",
# #                     "text": "You are an AI assistant that helps people find information."
# #                 }
# #             ]
# #         },
# #         {
# #             "role": "user",
# #             "content": "????? ??? ????????"  # The question in Arabic
# #         }
# #     ],
# #     "temperature": 0.7,
# #     "top_p": 0.95,
# #     "max_tokens": 800
# # }
# #
# # # Define the endpoint
# # GPT4V_ENDPOINT = "https://islam.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-02-15-preview"
# #
# # # Send request
# # try:
# #     response = requests.post(GPT4V_ENDPOINT, headers=headers, json=payload)
# #     response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
# # except requests.RequestException as e:
# #     raise SystemExit(f"Failed to make the request. Error: {e}")
# #
# # # Handle the response
# # response_json = response.json()
# # assistant_message = response_json['choices'][0]['message']['content']
# # print(f"Assistant's message: {assistant_message}")
#
#
# import os
# import requests
# import base64
#
# # Fetch API Key from environment variable
# GPT4V_KEY = os.getenv('GPT4V_API_KEY', '17bd4c377c8248f3a08bacb8c30e79c6')
# if not GPT4V_KEY:
#     raise ValueError("API key is missing. Please set the environment variable GPT4V_API_KEY.")
#
# # Define headers
# headers = {
#     "Content-Type": "application/json",
#     "api-key": GPT4V_KEY,
# }
#
# # Define the payload for the request
# payload = {
#     "messages": [
#         {
#             "role": "system",
#             "content": "??? ????? ??? ????? ????? ?? ?????? ??? ?????????. ??? ?? ???? ???? ?????? ?????? ???????."
#         },
#         {
#             "role": "user",
#             "content": "????? ??? ????????"  # The question in Arabic
#         }
#     ],
#     "temperature": 0.7,
#     "top_p": 0.95,
#     "max_tokens": 800
# }
#
# # Define the endpoint
# GPT4V_ENDPOINT = "https://islam.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-02-15-preview"
#
# # Send request
# try:
#     response = requests.post(GPT4V_ENDPOINT, headers=headers, json=payload)
#     response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
# except requests.RequestException as e:
#     raise SystemExit(f"Failed to make the request. Error: {e}")
#
# # Handle the response
# response_json = response.json()
# assistant_message = response_json['choices'][0]['message']['content']
# print(f"Assistant's message: {assistant_message}")


import torch
print(torch.__version__)
