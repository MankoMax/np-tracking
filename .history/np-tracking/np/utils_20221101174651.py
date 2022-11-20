import requests
import json

def get_ttn(ttn):
    url = 'https://api.novaposhta.ua/v2.0/json/'
    headers = {'content-type': 'application/json'}
    data = {
        "apiKey": "API_KEY",
        "modelName": "TrackingDocument",
        "calledMethod": "getStatusDocuments",
        "methodProperties": {
            "Documents": [
                {
                    "DocumentNumber": ttn,
                    "Phone": "380672425835"
                }
            ]
        }
    }
    response = requests.post(url, data=json.dumps(data), headers=headers)
    return response.json()
