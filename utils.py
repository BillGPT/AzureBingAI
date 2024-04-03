# utils.py
import json

# 从JSON响应中提取查询内容
def extract_query_from_json_response(json_response):
    function_call = json.loads(json_response)['function_call']
    arguments = json.loads(function_call['arguments'])
    query = arguments['query']
    return query

