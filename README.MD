# Project Name: AzureBingAI

## Description
AzureBingAI is an open-source project that integrates Azure OpenAI with the Bing Search API to provide a powerful and efficient search and response system. This system is capable of processing user input, performing web searches, and generating human-like responses in Chinese based on content extracted from the web in English.

## Function-calling Supported models
gpt-4, gpt-4-turbo-preview, gpt-4-0125-preview, gpt-4-1106-preview, gpt-4-0613, gpt-3.5-turbo, gpt-3.5-turbo-0125, gpt-3.5-turbo-1106, and gpt-3.5-turbo-0613

## Features
- Multilingual support: Accepts input in Chinese and provides responses in Chinese while performing searches in English.
- Integration with Azure OpenAI: Leverages the advanced capabilities of Azure OpenAI for natural language processing and response generation.
- Bing Search API integration: Utilizes the Bing Search API to fetch relevant URLs based on user queries.
- Web content extraction: Extracts and processes the content from the URLs returned by the Bing Search API for response generation.

## Installation

Before you can run the project, you need to install the necessary dependencies. You can do this by running the following command:

```bash
pip install -r requirements.txt
```

Make sure you have the following environment variables set in your `.env` file:

```plaintext
AZURE_OPENAI_API_KEY=your_azure_openai_api_key
AZURE_OPENAI_ENDPOINT=your_azure_openai_endpoint
BING_SEARCH_V7_SUBSCRIPTION_KEY=your_bing_search_v7_subscription_key
BING_SEARCH_V7_ENDPOINT=your_bing_search_v7_endpoint
```

## Usage

To use AzureBingAI, simply run the `main.py` script:

```bash
python main.py
```

The script will take a predefined user input, process it, perform a web search, extract content from the web, and generate a response in Chinese.

## How It Works

1. The user input is first processed by the `process_user_input` function in `azure_openai.py`, which sends the input to Azure OpenAI's GPT-3.5 Turbo model for initial processing.
2. The `extract_query_from_json_response` function in `utils.py` extracts the search query from the JSON response.
3. The `bing_search_urls` function in `bing_search.py` uses the Bing Search API to fetch URLs relevant to the query.
4. The `extract_content_from_urls` function processes these URLs to extract the text content.
5. The `generate_response` function in `azure_openai.py` uses the extracted content to generate a response that is contextually relevant to the original user input.

## TODO

- Implement a feature to adjust the order of search results from the Bing Search API (e.g., by time, relevance, etc.).
- Refine the prompt sent to Azure OpenAI to achieve better response quality.

## Contributions

Contributions are welcome! If you have a suggestion or improvement, please feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
