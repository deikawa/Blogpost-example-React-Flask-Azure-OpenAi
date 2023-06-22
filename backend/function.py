import os
import openai
from dotenv import load_dotenv

systemMessage = {
    "role": "system",
    "content": "You are a sophisticated Language Model developed to assist in managing blog posts. "
    "You have been trained on a diverse range of topics and possess extensive knowledge about writing,"
    " formatting, and optimizing blog content. You are designed to provide guidance on various aspects of blogging,"
    " including topic ideas, writing tips, SEO optimization, and engagement strategies. "
    "You can also help with proofreading, editing, and structuring blog posts to ensure they are engaging and well-organized. "
    "Feel free to ask for assistance with any aspect of creating compelling blog content!"
}

load_dotenv()

deployment_name = 'REPLACE_ME'
openai.api_type = 'azure'
openai.api_key = os.getenv('AZURE_OPENAI_API_KEY')
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT") # your endpoint should look like the following https://YOUR_RESOURCE_NAME.openai.azure.com/
openai.api_version = '2023-03-15-preview'

def generate_chat_response(prompt):
    messages = [systemMessage, {"role": "user", "content": prompt}]

    result = openai.ChatCompletion.create(
        engine="gpt-35-turbo",
        messages= messages,
        temperature=0.95,
        max_tokens=150,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )
    return result['choices'][0]['message']['content']
