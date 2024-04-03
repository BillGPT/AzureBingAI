# azure_openai.py
import os
from dotenv import load_dotenv

load_dotenv()

from openai import AzureOpenAI

# 定义一个处理用户输入的函数，该函数接收用户输入的内容，并返回处理后的JSON数据
def process_user_input(input_content):
    client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
    api_version="2023-10-01-preview",
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    )

    messages= [
        {"role": "assistant", "content": "生成准确的英文关键词"},
        {"role": "user", "content": input_content}
    ]

    functions= [
        {
            "name": "bing_search",
            "description": "Performs a search using Bing Search API",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query"
                    },
                    "mkt": {
                        "type": "string",
                        "description": "Market code for the query (i.e. en-US)"
                    }
                },
                "required": ["query"]
            }
        }
    ]

    response = client.chat.completions.create(
        model="gpt-35-turbo-16k", # model = "deployment_name"
        messages= messages,
        functions = functions,
        function_call={"name": "bing_search"},
    )

    return response.choices[0].message.model_dump_json(indent=2)

# 定义一个处理多轮对话的函数，该函数接收用户输入的内容和上一轮对话的结果，并返回处理后的JSON数据
def process_multi_turn(input_content, text_content):
    client = AzureOpenAI(
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        api_version="2023-10-01-preview",
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
    )

    messages = [
        {"role": "assistant", "content": "你要用中文回答"},
        {"role": "user", "content": input_content},
        {"role": "user", "content": "网页查询结果为:" + text_content + "你开始回答："}
    ]

    functions = [
        {
            "name": "bing_search",
            "description": "Performs a search using Bing Search API",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query"
                    },
                    "mkt": {
                        "type": "string",
                        "description": "Market code for the query (i.e. en-US)"
                    }
                },
                "required": ["query"]
            }
        }
    ]

    response = client.chat.completions.create(
        model="gpt-35-turbo-0613",
        messages=messages,
        functions=functions,
        function_call="auto"
    )

    return response.choices[0].message.content
