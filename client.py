from openai import OpenAI
import os

client = OpenAI(
    api_key = ''
)


completion = client.chat.completions.create(
    model = 'gpt-3.5-turbo',
    messages = [
        {'role': 'system', 'content':'you are a virtual assistant named jarvis in general tasks like alexa and Google'},
        {'role': 'user', 'content':'what is coding'}
    ]
)

print(completion.choices[0].message)

# response = client.responses.create(
#     model="gpt-5",
#     input="Write a one-sentence bedtime story about a unicorn."
# )

# print(response.output_text)


# response = client.responses.create(
#     model="gpt-5",
#     input=[
#         {
#             "role": "user",
#             "content": [
#                 {
#                     "type": "input_text",
#                     "text": "What teams are playing in this image?",
#                 },
#                 {
#                     "type": "input_image",
#                     "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/3b/LeBron_James_Layup_%28Cleveland_vs_Brooklyn_2018%29.jpg"
#                 }
#             ]
#         }
#     ]
# )

# print(response.output_text)

#this code defaults to getting the API key using os.environ.get("OPEN_API_KEY")

#if you saved the key under a different environment variable name, you can do something like:

#client = OpenaI(api_key = os.environ.get("KEY name for this"))




