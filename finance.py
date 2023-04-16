import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('NYT_API_KEY')
api_key2 = os.getenv('G_API_KEY')
api_key3 = os.getenv('NEWS_API_KEY')

# url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
# params = {
#     "q": "tesla",
#     "api-key": api_key
# }

# response = requests.get(url, params=params)

def newsAPI():

    base_url = "https://newsapi.org/v2/everything"
    params = {
        "q": "TESLA",
        "from": "2023-04-01",
        "sortBy": "popularity",
        "apiKey": api_key3
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    # Extract the fields of interest from each article
    articles = []
    for article in data["articles"]:
        article_data = {
            "author": article["author"],
            "title": article["title"],
            "description": article["description"],
            "url": article["url"],
            "urlToImage": article["urlToImage"],
            "publishedAt": article["publishedAt"],
            "content": article["content"]
        }
        articles.append(article_data)

    # Save the extracted data to a JSON file
    with open("newsapi.json", "w") as file:
        json.dump(articles, file, indent=4)

def guardian():
    base_url = "https://content.guardianapis.com/search"
    params = {
        "page": "2",
        "q": "tesla",
        "api-key": api_key2
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    # Extract the fields of interest from each result
    results = []
    for result in data["response"]["results"]:
        result_data = {
            "id": result["id"],
            "type": result["type"],
            "sectionId": result["sectionId"],
            "sectionName": result["sectionName"],
            "webPublicationDate": result["webPublicationDate"],
            "webTitle": result["webTitle"],
            "webUrl": result["webUrl"],
            "apiUrl": result["apiUrl"],
            "isHosted": result["isHosted"],
            "pillarId": result["pillarId"],
            "pillarName": result["pillarName"]
        }
        results.append(result_data)

    # Save the extracted data to a JSON file
    with open("guardian.json", "w") as file:
        json.dump(results, file, indent=4)

def nyt():
    url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
    params = {
        "q": "tesla",
        "api-key": api_key
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        articles = data["response"]["docs"]
        parsed_data = []
        for article in articles:
            parsed_article = {
                "abstract": article['abstract'].replace('\u2019', "'"),
                "web_url": article['web_url'].replace('\u2019', "'"),
                "snippet": article['snippet'].replace('\u2019', "'"),
                "lead_paragraph": article['lead_paragraph'].replace('\u2019', "'"),
                "source": article.get("source", ""),
                "pub_date": article.get("pub_date", ""),
                "document_type": article.get("document_type", ""),
                "news_desk": article.get("news_desk", ""),
                "section_name": article.get("section_name", "")
            }
            parsed_data.append(parsed_article)
        with open(os.path.join(os.getcwd(), "nyt.json"), "w") as f: #nyt_articles.json filename to save parsed data
            json.dump(parsed_data, f, indent=4)
    else:
        print("Error: Could not retrieve articles.")

nyt()
guardian()
newsAPI()

# abstract, web_url, snippet, lead_paragraph, source, pub_date, document_type, news_desk, section_name
# https://content.guardianapis.com/search?page=2&q=tesla&api-key=0ba289a8-884e-4fbb-af88-bd5b409cbcae