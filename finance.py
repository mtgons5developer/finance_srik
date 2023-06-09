import requests
import json
import os
import time
import openai
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()

api_key = os.getenv('NYT_API_KEY')
api_key2 = os.getenv('G_API_KEY')
api_key3 = os.getenv('NEWS_API_KEY')
openai.api_key = os.getenv("OPENAI_API_KEY")

def openAI():
    question = "Decide whether a News sentiment is positive, neutral, or negative. News: "
    message = "Elon Musk, the chief executive of Tesla, announced on Twitter on Sunday that his company would build a factory in Shanghai with the aim to assemble 10,000 giant batteries annually for electric producers and distributors."
    # summarize = openai.Completion.create(
    # model="text-davinci-003",
    # prompt=message,
    # max_tokens=7,
    # temperature=0
    # )
    # print(summarize)

    sentiment = openai.Completion.create(
    model="text-davinci-003",
    prompt=question + message,
    temperature=0,
    max_tokens=60,
    top_p=1,
    frequency_penalty=0.5,
    presence_penalty=0
    )
    print(sentiment)
    print(question + message)

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

def ms():

    chrome_driver_path = '/chromedriver2'
    driver = webdriver.Chrome(executable_path=chrome_driver_path)

    driver = webdriver.Chrome() # or other webdriver
    driver.get("https://www.morningstar.com/stocks/xnas/tsla/financials")

    # Wait for the Export Data button to be clickable
    export_button = driver.find_element(By.XPATH, "//a[@class='export-data ']")
    export_button.click()

    # Wait for the file to download (adjust sleep time as needed)
    time.sleep(10)

    # Get the path of the downloaded file in your default downloads folder
    default_downloads_path = os.path.expanduser("")
    downloaded_file = max([os.path.join(default_downloads_path, f) for f in os.listdir(default_downloads_path)], key=os.path.getctime)

    # Move the file to a new location
    new_location = ""
    new_file_name = "tsla_financials.csv"
    new_file_path = os.path.join(new_location, new_file_name)
    os.rename(downloaded_file, new_file_path)

openAI()
# ms()
# nyt()
# guardian()
# newsAPI()
