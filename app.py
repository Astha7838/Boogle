from flask import Flask ,render_template,request,jsonify 
from elasticsearch import Elasticsearch
import warnings


#host = 'https://tux-es2.cci.drexel.edu:9200/'
warnings.filterwarnings("ignore")
#es = Elasticsearch(hosts=host,verify_certs=False,http_auth='at3358:icho3oop9nei',connection_class=RequestsHttpConnection,)


es = Elasticsearch(
    cloud_id="Boogle:dXMtZWFzdDQuZ2NwLmVsYXN0aWMtY2xvdWQuY29tJDExMTVlMzg5MmYzNzQxYWFiNzU3Y2QyZjA5OWM0MmUzJGEzMWUyNDQ2MzNlNDRjMmZiYzNiNGNmODUzMTc1Yjg3",
    http_auth=("elastic", "2ujXDZHRnxnFYHBblQtubdEq"),
)

app = Flask(__name__)
#AIzaSyDgVyqZBnpNyoEC-U44rPw_f9KgRG_JSyA

@app.route("/")
def test():
    return render_template("search.html")

@app.route('/search', methods=['POST'])
def search():
    keywords = request.form['keywords']
    query_body = {
        "query": {
            "multi_match": {
                "query": keywords,
                "fields": ["description", "title","authors"]
            }
        }
    }
    res=es.search(index='at3358_info624_201904_boogle_reindex', doc_type='_doc',body=query_body)
    #return jsonify(res['hits']['hits'])
    response_data=res['hits']['hits']
    return render_template("results.html",res=response_data)

if __name__ == '__main__':
   app.run(host="0.0.0.0",port=8005)