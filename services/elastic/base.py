from elasticsearch import helpers

from connection import connection


class BaseModelCrud():
    es = connection()
    index_name = "item"

class CreateModel(BaseModelCrud):

    def create_index(self):
        try:
            index_exists = self.es.indices.exists(index=self.index_name)

            if not index_exists:
                self.es.indices(index=self.index_name)
                print("Index muvaffaqiyatli yaratildi")

        except Exception as e:
            print("Elasticsearch xatosi: ", e)

    def create(self):
        try:
            doc = {"item_name": "orange", "price": 200}
            self.es.index(index=self.index_name, document=doc, id=1)
            print("bitta hujjat qo'shildi!!")
        except Exception as err:
            print("Hujjat yaratishda xato ", err)


class SearchModel(BaseModelCrud):
    range_query = {"query": {"range": {"price": {"gte": 100}}}}

    def search_index(self):

        try:
            results = self.es.search(index=self.index_name)
            for i in range(len(results["hits"]["hits"])):
                print("Qidiruv natijalari: ", results["hits"]["hits"][i]["_source"])

        except Exception as e:
            print("Qidiruv xatosi: ", e)



    def search_count(self):

        try:
            results = self.es.search(index=self.index_name, query=self.range_query)
            print("Qidiruv natijalari soni: ", len(results["hits"]["hits"]))

        except Exception as e:
            print("Natijaalar sonini ko'rsatishda xato: ", e)

        try:
            results = self.es.search(index=self.index_name, query=self.range_query, size=1000)
            print("Maxsus o'lchamli qidiruv natijalari soni", len(results["hits"]["hits"]))

        except Exception as e:
            print("Natijalar sonini ko'rsatishda xato: ", e)

        try:
            results = helpers.scan(client=self.es, query=self.range_query, index=self.index_name)
            count = 0
            for result in results:
                count += 1
            print("Helpers Scan yordamida qidiruv natijalari soni ", count)
        except Exception as e:
            print("Natijalar sonini ko'rsatishda xato ", e)

class UpdateModel(BaseModelCrud):
    def update(self):
        try:
            doc = self.es.search(index=self.index_name)

            for i in doc["hits"]["hits"]:
                doc_body = i["_source"]
                doc_id = i["_id"]
                doc_body["price"] = 50
                self.es.update(index=self.index_name, id=doc_id, doc=doc_body)
                print("Hujjat muvaffaqiyatli yangilandi!")
        except Exception as err:
            print("Qidiruv bilan yangilashda xato: ", err)

class DeleteModel(BaseModelCrud):
    def delete(self, id):
        try:
            self.es.delete(index=self.index_name, id = id)
            print("Hujjat soʻrov asosida muvaffaqiyatli oʻchirildi!")
        except Exception as err:
            print("Oʻchirishda xato: ", err)

