from elasticsearch import Elasticsearch
import json, requests

# construct dictionary to pass into search method

elastic_client = Elasticsearch()
search_param = {
    "query": {
        "match": {
            "field1": "find me!"
        }
    }
}
print(search_param)


some_string = '{"hello" : "world"}'
some_dict = json.loads(some_string)
print (type(some_dict))
print (some_dict["hello"])

item_id = "U492023"

# pass into a dictionary
search_param = {
    "query": {
        "terms": {
            "_id": [item_id]
        }
    }
}

search_param = {
    "query": {
        "terms": {
            "_id": [ 1234, 42]

        }
    }
}

response = elastic_client.search(index="some_index", body=search_param)
print("response":, response)
