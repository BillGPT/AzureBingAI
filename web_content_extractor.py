# web_content_extractor.py
from bs4 import BeautifulSoup
import requests

def extract_content_from_urls(urls):
    # 设置请求头中的User-Agent，模拟浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    url = urls[0]

    # 发送GET请求
    response = requests.get(url, headers=headers)

    # 使用BeautifulSoup解析HTML并提取文本内容
    soup = BeautifulSoup(response.text, 'html.parser')
    text_content = soup.get_text()

    # 过滤掉换行符
    text_content = text_content.replace('\n', '')

    return text_content
