# Topic-Modelling-for-the-EA-2021

**Introduction:** 

The environment is a crucial consideration in business, and compliance with environmental regulations is essential for companies operating in industries that may have a significant impact on the environment. The Environmental Act of 2021 is a significant statute that establishes rules for environmental protection, and compliance with this law is particularly important for organizations like Capgemini that work in a range of industries. To ensure compliance, it is important to identify potential areas of non-compliance through the analysis of various text corpora, such as documents related to waste disposal, pollution control, and wildlife conservation. This analysis can help companies identify potential areas of non-compliance and take appropriate action to ensure they are operating in an environmentally sustainable manner. 
\section*{\small Approach}

This dissertation aims to use unsupervised learning techniques, specifically topic modeling, to analyze large text corpora related to environmental compliance. The corpus will consist of various documents, such as regulatory guidelines, internal company policies, and incident reports related to waste disposal, pollution control, and wildlife conservation.


To build a proof of concept, the study will explore four main techniques, including Latent Dirichlet Allocation, Top2Vec, Bertopic, and Non-Matrix Factorization. These techniques were chosen based on the comparison work of Egger and Yu (2022), which found that BERTopic and NMF were the most potent algorithms, followed by Top2Vec and LDA.


One of the key goals of this experiment is to explore how different methods work on a granular level and experiment with various pre-processing techniques and ensembles to obtain the best possible results. By comparing and combining the outputs of multiple algorithms, we can achieve a more comprehensive understanding of the text.


For example, NMF and LDA rely on bag-of-words representations, which do not take into account the order of words. As a result, these techniques require the exclusion of stop words, tokenization, and stemming. On the other hand, BERTopic and Top2Vec use embedding approaches that do not require these preprocessing steps and can handle stop words without affecting the resulting embeddings.


By using multiple algorithms with different approaches to text analysis, we can capture a wider range of semantic relationships within the text. The word frequency approach of NMF and LDA, for instance, captures different semantic relationships than the distributed representation approach used by Top2Vec and BERTopic. Combining the results of these algorithms can help us gain a more nuanced understanding of the underlying themes and topics present in the text.


**Conclusion:** 
By exploring different preprocessing techniques and ensembles, this dissertation aims to provide insights into how unsupervised learning techniques can be used to analyze large text corpora related to environmental compliance. Additionally, it aims to demonstrate how different preprocessing steps can impact the results of different techniques. Overall, this research will help companies identify potential areas of non-compliance with environmental regulations and take appropriate action to ensure they are operating sustainably.

**sources:** 
Egger, Roman, and Joanne Yu. ‘A Topic Modeling Comparison Between LDA, NMF, Top2Vec, and BERTopic to Demystify Twitter Posts’. Frontiers in Sociology 7 (6 May 2022): 886498. https://doi.org/10.3389/fsoc.2022.886498.

# Getting started

**Step 1**: Install depencies by running 'pip install -r requirements.txt'

**Step 2**:Scrape the URL from the GOV.uk website by running: 
‘scrapy runspider myspider.py -o articles.json’

Note: the search will start from this link and iterate through every next page to gather links of all the articles:  
	
https://www.gov.uk/search/news-and-communications?keywords=environment&order=relevance&page=1

You can change the start link in the spyder.py file. Additionally, the articles.json file is already included in the repo should you want to avoid running it. 


**Step 2**: Read the URL and scrape them with bs4
-	‘python Web_Scraper.py articles.json’

Note: the output will be in the Unstructured_Corpora.txt file.
