import warnings
from datetime import datetime

from elasticsearch import helpers

from connection import connection

doc = {
    'author': 'author_name',
    'text': 'Interensting content...',
    'timestamp': datetime.now(),
}

def create_index():
    es = connection()
    index_name = "item"

    try:
        index_exists = es.indices.exists(index=index_name)

        if not index_exists:
            es.indices(index=index_name)
            print("Index muvaffaqiyatli yaratildi")

    except Exception as e:
        print("Elasticsearch xatosi: ", e)

def create():
    es = connection()
    index_name = "item"

    try:
        doc = {"item_name": "orange", "price": 200}
        es.index(index=index_name, document=doc, id=1)
        print("bitta hujjat qo'shildi!!")
    except Exception as err:
        print("Hujjat yaratishda xato ", err)

    try:
        docs = [
            {"item_name": "apple", "price": 100},
            {"item_name": "mango", "price": 150},
            {"item_name": "mandarin", "price": 200},
            {"item_name": "lemon", "price": 250},
            {"item_name": "chips", "price": 300},
            {"item_name": "chocolate", "price": 550},
            {"item_name": "banana", "price": 220}
        ]
        helpers.bulk(es, docs, index=index_name)
        print("bir nechta hujjatlar qo'shildi!!")
    except Exception as err:
        print("Bir nechta hujjat yaratishda xato ", err)

def read():
    es = connection()
    index_name = "item"

    try:
        results = es.search(index=index_name)
        for i in range(len(results["hits"]["hits"])):
            print("Qidiruv natijalari: ", results["hits"]["hits"][i]["_source"])

    except Exception as e:
        print("Qidiruv xatosi: ", e)

    range_query = {"query": {"range": {"price": {"gte": 100}}}}

    try:
        results = es.search(index=index_name, query=range_query)
        print("Qidiruv natijalari soni: ", len(results["hits"]["hits"]))

    except Exception as e:
        print("Natijaalar sonini ko'rsatishda xato: ", e)

    try:
        results = es.search(index=index_name, query=range_query, size=1000)
        print("Maxsus o'lchamli qidiruv natijalari soni", len(results["hits"]["hits"]))

    except Exception as e:
        print("Natijalar sonini ko'rsatishda xato: ", e)

    try:
        results = helpers.scan(client=es, query=range_query, index = index_name)
        count = 0
        for result in results:
            count += 1
        print("Helpers Scan yordamida qidiruv natijalari soni ", count)
    except Exception as e:
        print("Natijalar sonini ko'rsatishda xato ", e)

def search_source():
    es = connection()
    index_name = "item"
    try:
        results = es.search(index=index_name)
        print("Qidiruv natijalari soni: ", len(results["hits"]["hits"]))

    except Exception as e:
        print("Natijaalar sonini ko'rsatishda xato: ", e)

def update():
    es = connection()
    index_name = "item"

    try:
        doc = es.search(index=index_name)

        for i in doc["hits"]["hits"]:
            doc_body = i["_source"]
            doc_id = i["_id"]

            doc_body["price"] = 50
            es.update(index=index_name, id=doc_id, doc=doc_body)
            print("Hujjat muvaffaqiyatli yangilandi!")
    except Exception as err:
        print("Qidiruv bilan yangilashda xato: ", err)

    # try:
    #     doc_results = helpers.scan(client=es, query=doc_body, index=index_name)
    #
    #     for doc in doc_results:
    #         doc_body = doc["_source"]
    #         doc_id = doc["_id"]
    #
    #         doc_body["price"] = 22
    #         es.update(index=index_name, id=doc_id, query={"doc": doc_body})
    #         print("Hujjat muvaffaqiyatli yangilandi!")
    # except Exception as err:
    #     print("Skanerlash bilan yangilashda xato: ", err)

def delete():
    es = connection()
    index_name = "item"
    # es.delete(index=index_name, id="foIJSoMBhXyCiLCqX7R5")
    # print("o'chirildi")

    query = {"query": {"term": {"product_name": "chips"}}}
    try:
        es.delete_by_query(index=index_name, query=query)
        print("Hujjat soʻrov asosida muvaffaqiyatli oʻchirildi!")
    except Exception as err:
        print("Oʻchirishda xato: ", err)

read()