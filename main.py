# main.py

import os
import json
from dotenv import load_dotenv
from openai import AzureOpenAI
from azure_openai import process_user_input, process_multi_turn
from bing_search import bing_search_urls
from web_content_extractor import extract_content_from_urls
from utils import extract_query_from_json_response

load_dotenv()

# 主程序调用函数获取用户输入并处理
if __name__ == "__main__":
    #user_input = get_user_input()
    user_input = "Bing Search API如何设置排序参数"
    result = process_user_input(user_input)
    print("result:\n")
    print(result)

    query = extract_query_from_json_response(result)
    print("query:\n")
    print(query)

    urls = bing_search_urls(query)
    print("urls:\n")

    print(urls)
    #urls = ['https://mining-provider.com/get-ready-for-the-future-kaspa-mining-in-2024/']
    text_content = extract_content_from_urls(urls)
    print("text_content:\n" + text_content)

    result2 = process_multi_turn(user_input, text_content)
    print("result2:\n" + result2)
