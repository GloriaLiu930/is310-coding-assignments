import requests
import json


meowfacts_url = "https://meowfacts.herokuapp.com/"
response_meowfacts = requests.get(meowfacts_url)
if response_meowfacts.status_code == 200:
    meowfact_data = response_meowfacts.json()
    print("MeowFact:", meowfact_data)
    search_term = meowfact_data["data"][0]
else:
    print("Failed to retrieve data from MeowFacts API.")

europeana_base_url = "https://www.europeana.eu/api/v2/search.json"
europeana_api_key = "Your-API-keys"  # Replace with your API key here
params = {
    "wskey": europeana_api_key,
    "query": search_term,
    "rows": 1
}
response_europeana = requests.get(europeana_base_url, params=params)
if response_europeana.status_code == 200:
    europeana_data = response_europeana.json()
    print("Europeana Data:", europeana_data)
else:
    print("Failed to retrieve data from Europeana.")

filtered_data = {
    "MeowFact Data": meowfact_data,
    "Europeana Data": europeana_data.get("items", [])
}
with open("meowfact_europeana_data.json", "w") as json_file:
    json.dump(filtered_data, json_file, indent=4)

print("Data saved to meowfact_europeana_data.json")