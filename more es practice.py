import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch()
client = Elasticsearch(hosts=["localhost :10.0.0.93"])
dir(client)
index_name = "some_index"
doc_id = 1234
index_exists = client.indices.exists(index=index_name)
if index_exists == False:
    print("index_name:", index_name, "does not exist.")
elif index_exists == True:
    print("index_name", index_name, "exists.")
