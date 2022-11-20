import requests
import json

def get_ttn(ttn, phone):
    url = 'https://api.novaposhta.ua/v2.0/json/'
    headers = {'content-type': 'application/json'}
    if type(ttn) == str:
        data = {
            "apiKey": "",
            "modelName": "TrackingDocument",
            "calledMethod": "getStatusDocuments",
            "methodProperties": {
                "Documents": [
                    {
                        "DocumentNumber": ttn,
                        "Phone": phone
                    }
                ]
            }
        }
    elif type(ttn) == list:
        documents = []
        for i in ttn:
            documents.append({"DocumentNumber": i, "Phone": phone})
        data = {
            "apiKey": "",
            "modelName": "TrackingDocument",
            "calledMethod": "getStatusDocuments",
            "methodProperties": documents
        }
    response = requests.post(url, data=json.dumps(data), headers=headers)
    return response.json()
