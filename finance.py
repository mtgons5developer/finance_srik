import requests
import json

url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
params = {
    "q": "tesla",
    "api-key": "RJNXuH7mLBG5gb9OhlaruyyRkvqMyCL1"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    with open('nyt_articles.json', 'w') as f:
        json.dump(data, f)
else:
    print("Error retrieving data from API")
