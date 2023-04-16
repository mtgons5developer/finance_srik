import requests
import json

base_url = "https://content.guardianapis.com/search"
params = {
    "page": "2",
    "q": "tesla",
    "api-key": "0ba289a8-884e-4fbb-af88-bd5b409cbcae"
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
with open("tesla_articles.json", "w") as file:
    json.dump(results, file, indent=4)
