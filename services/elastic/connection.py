from elasticsearch import Elasticsearch

URL = "http://localhost:9200"

def connection():
    es = Elasticsearch(URL, basic_auth=('elastic', "nmK7*575lnH7kP_Ml91O"))
    return es