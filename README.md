# Topic-Modelling-for-the-EA-2021

**Step 1**: Scrape the URL from the GOV.uk website by running: 
‘scrapy runspider myspider.py -o articles.json’

Note: the search will start from this link and iterate through every next page to gather links of all the articles:  
	
https://www.gov.uk/search/news-and-communications?keywords=environment&order=relevance&page=1

You can change the start link in the spyder.py file. Additionally, the articles.json file is already included in the repo should you want to avoid running it. 


**Step 2**: Read the URL and scrape them with bs4
-	‘python Web_Scraper.py articles.json’

Note: the output will be in the Unstructured_Corpora.txt file.
