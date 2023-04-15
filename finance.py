import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('NYT_API_KEY')

url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
params = {
    "q": "tesla",
    "api-key": api_key
}

response = requests.get(url, params=params)

# if response.status_code == 200:
#     data = response.json()
#     with open('nyt_articles.json', 'w') as f:
#         json.dump(data, f)
# else:
#     print("Error retrieving data from API")

if response.status_code == 200:
    data = response.json()
    articles = data["response"]["docs"]
    parsed_data = []
    for article in articles:
        parsed_article = {
            "abstract": article.get("abstract", ""),
            "web_url": article.get("web_url", ""),
            "snippet": article.get("snippet", ""),
            "lead_paragraph": article.get("lead_paragraph", ""),
            "source": article.get("source", ""),
            "pub_date": article.get("pub_date", ""),
            "document_type": article.get("document_type", ""),
            "news_desk": article.get("news_desk", ""),
            "section_name": article.get("section_name", "")
        }
        parsed_data.append(parsed_article)
    with open(os.path.join(os.getcwd(), "nyt_articles.json"), "w") as f:
        json.dump(parsed_data, f, indent=4)
else:
    print("Error: Could not retrieve articles.")

# abstract, web_url, snippet, lead_paragraph, source, pub_date, document_type, news_desk, section_name