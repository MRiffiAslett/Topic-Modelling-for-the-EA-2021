import json
import requests
from bs4 import BeautifulSoup
import sys

# read the JSON file and load its contents
with open(sys.argv[1], 'r') as f:
    json_data = json.load(f)

# extract the URLs from the JSON data
URL = [data["url"] for data in json_data]

# scrape the web pages
full_text = []
for url in URL:
    responses = requests.get(url)
    page_content = responses.content
    soup = BeautifulSoup(page_content, 'html.parser')
    text = soup.get_text().replace('\n','')
    full_text.append(text)

# write the scraped content to a file
with open('Unstructured_Corpora.txt', 'w') as f:
    f.write('\n'.join(full_text))

print(f'{len(URL)} pages scraped. The output is in a file called output.txt.')