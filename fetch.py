import requests
from elasticsearch import Elasticsearch
import json
import random
import warnings

#host = 'https://tux-es2.cci.drexel.edu:9200/'
warnings.filterwarnings("ignore")
#es = Elasticsearch(hosts=host,verify_certs=False,http_auth='at3358:icho3oop9nei',connection_class=RequestsHttpConnection,)

es = Elasticsearch(
    cloud_id="Boogle:dXMtZWFzdDQuZ2NwLmVsYXN0aWMtY2xvdWQuY29tJDExMTVlMzg5MmYzNzQxYWFiNzU3Y2QyZjA5OWM0MmUzJGEzMWUyNDQ2MzNlNDRjMmZiYzNiNGNmODUzMTc1Yjg3",
    http_auth=("elastic", "2ujXDZHRnxnFYHBblQtubdEq"),
)
#creating an below index with respective settings

index_name = 'at3358_info624_201904_boogle_reindex'
request_body = {
        "settings":{
            "index":{
                "similarity":{
                    "custom_bm25":{
                        "type": "BM25",
                        "k1": 2.0,
                        "b":1.0
                    },
                    "custom_dfr":{
                        "type": "DFR",
                        "basic_model": "g",
                        "after_effect": "l",
                        "normalization": "h2",
                        "normalization.h2.c": "3.0"
                    }
                }
            }
    },
 
        'mappings': {
            
            "properties":{
                "authors":{
                    "type": "text" ,
                    "analyzer": "standard",
                    "similarity": "boolean"
                    },
                "description":{
                    "type": "text" ,
                    "analyzer": "english",
                    "similarity":"custom_dfr"
                    },
                  "id" : {
                  "type" : "long"
                },
                "infoLink":{
                    "type": "text"
                    },
                "previewLink":{
                    "type": "text"
                    },
                "title":{
                    "type": "text" ,
                    "analyzer": "english",
                    "similarity":"custom_bm25"
                    },

                }
            }
        }
es.indices.create(index = index_name, body = request_body)

i=1
books_list=["python","R","information science","AI","deep learning","elastic search","information retrieval","image processing","search engine",'reactjs',"html",
           "server side","javascript","Data Mining","nference and Prediction","data analysis","cloud computing","client side","ethical hacking","Statistical Learning"
           "Pattern Recognition and Machine Learning","mathematics for machine learning","coding","c++","C#","java","scripting languages","linux","unix","virtual environment"]
for book in books_list:
    books = requests.get("https://www.googleapis.com/books/v1/volumes?q=" +
                            book +
                            "&maxResults=40&key=AIzaSyCjewB8JaZil--qGlfSy8aZf0QVL4qK5jQ").json()
    r = json.dumps(books)
    loaded_books = json.loads(r)
    dict_book={}
   
    for item in loaded_books["items"]:
        try:
            dict_book["id"]=i
            if "title" not in item["volumeInfo"]:
                dict_book["title"]='NA'
            else:
                dict_book["title"]=item["volumeInfo"]["title"]
            if "description" not in item["volumeInfo"]:
                dict_book["description"]='NA'
            else:
                dict_book["description"]=item["volumeInfo"]["description"]
            if "authors" not in item["volumeInfo"]:
                dict_book["authors"]='NA'
            else:
                dict_book["authors"]=item["volumeInfo"]["authors"]
            if "previewLink" not in item["volumeInfo"]:
                dict_book["previewLink"]="NA"
            else:
                dict_book["previewLink"]=item["volumeInfo"]["previewLink"]
            if "infoLink" not in item["volumeInfo"]:
                dict_book["infoLink"]="NA"
            else:
                dict_book["infoLink"]=item["volumeInfo"]["infoLink"]
            
            es.index(index='at3358_info624_201904_boogle', doc_type='book',id=i,  body=dict_book)
            print(i)
            i=i+1

        except:
            continue;

    
print("Done!")

result = es.reindex({
        "source": {"index": "at3358_info624_201904_boogle"},
        "dest": {"index": "at3358_info624_201904_boogle_reindex"}
    }, wait_for_completion=True, request_timeout=300)

   



