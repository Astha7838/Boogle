BOOGLE: TECHNICAL BOOKS SEARCH ENGINE


Introduction: 
Let us  think how does the Google search the entire internet with what ever we type in the search bar.? And it gives the relevant result for the search even if we misspell it. Similarly, not only Google even the Wikipedia , how does the Wikipedia sort though 5+ million articles to find the most relevant one with our search keywords.?  
To understand the basic background process of these questions, we have set up full-text customized search application ( obviously not a high level as Google) , our example app will provide a UI and API to search the complete texts of 1000+ technical Books.

Methodology:

1. Extraction

1.1 Identifying the application:We have used personal API key for authorization to fetch list of books in JSON format. 
Few example in the list of Books: "python","R","information science","AI","deep learning","elastic search","information retrieval“ etc.

1.2 Fetching data from Google API:Based on the list of technical books provided and requests module of python, we are fetching around 1000+ books . The response is in JSON format so, after processing the response we are take out Title, Description, Authors, preview Link and Info link of the books.

1.3 Inserting data to elastic search by creating indexes.

2. Similarity 

2.1 Re-indexing based on custom Similarity:
Re-indexing the current index based on different custom similarity. We'll calculate precision and recall values based on different custom similarity and select the best similarity measure to re-index the indexes.

3. Implementation

3.1 Created an interactive web application that will let a user to search technical books in the customized search engine.

Technologies used : 
Flask web framework
HTML for templates. 
CSS for styling
Heroku for deploying

A. STEPS TO START APPLICATION in LOCAL ENVIRONMENT:

1. Clone the repository or download zip folder
2. unzip the files
3.On console/terminal navigate to project directory
4. Run the command -
4.1 On MAC run this command in terminal : source env/bin/activate
4.2 On windows run this command in console  : .\venv\Scripts\activate

5. Run python app.py
6. open http://0.0.0.0:8005/ in browser.

NOTE: Drexel cisco VPN should be connected .

B. STEPS TO DEPLOY APPLICATION ON HEROKU:

Currently, the usage of the Drexel account would require VPN, Cisco to be specific, in order to access the provided TUX URL. This would work in a local environment, but upon deployment, the URL would not be accessible because of the lack of VPN. Therefore, we can create a personal trial account, valid only for 15 days, in order to make use of ElasticSearch.

https://www.geeksforgeeks.org/deploy-python-flask-app-on-heroku/

https://learn.dcollege.net/ultra/courses/_262343_1/cl/outline

You need to sign up here :https://cloud.elastic.co/registration?elektra=downloads-overview&storm=elasticsearch%20 

APPLICATION LINK : https://boogle123.herokuapp.com/
