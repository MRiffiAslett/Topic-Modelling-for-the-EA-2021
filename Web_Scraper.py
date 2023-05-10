import json
import requests
from bs4 import BeautifulSoup
import sys

# read the JSON file and load its contents
with open(sys.argv[1], 'r') as f:
    json_data = json.load(f)

# extract the URLs from the JSON data
URLs = [data["url"] for data in json_data]

# scrape the web pages and add the text to the JSON data
for i, url in enumerate(URLs):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text().replace('\n','')
    json_data[i]["content"] = text

# write the updated JSON data to a new file
with open('updated_' + sys.argv[1], 'w') as f:
    json.dump(json_data, f, indent=2)

print(f'{len(URLs)} pages scraped and added to the new JSON file.')
