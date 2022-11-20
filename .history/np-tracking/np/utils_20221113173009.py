import requests
import json

def get_ttn(ttn, phone):
    url = 'https://api.novaposhta.ua/v2.0/json/'
    headers = {'content-type': 'application/json'}
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
    response = requests.post(url, data=json.dumps(data), headers=headers)
    return response.json()
