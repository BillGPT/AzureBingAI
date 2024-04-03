# bing_search.py

import os
import requests
from dotenv import load_dotenv

load_dotenv()

def bing_search_urls(query):
    subscription_key = os.getenv('BING_SEARCH_V7_SUBSCRIPTION_KEY')
    endpoint = os.environ['BING_SEARCH_V7_ENDPOINT'] + "/v7.0/search"

    mkt = 'en-US'
    params = { 'q': query, 'mkt': mkt }
    headers = { 'Ocp-Apim-Subscription-Key': subscription_key }

    try:
        response = requests.get(endpoint, headers=headers, params=params)
        response.raise_for_status()

        json_response = response.json()
    except Exception as ex:
        raise ex

    urls = [item['url'] for item in json_response['webPages']['value']]
    return urls