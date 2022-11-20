import requests
import json

def get_ttn(ttn, phone=None):
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
            "methodProperties": {
                "Documents": documents
            }
        }
    else:
        return 'Wrong type'
    response = requests.post(url, data=json.dumps(data), headers=headers)
    result = parse_info(response.json())
    return result


def parse_info(info):
    if info['success']:
        info = info['data'][0]
        return {
            'ttn': info['Number'],
            'status': info['Status'],
            'sent_date': info['DateCreated'],
            'schedule_date': info['ScheduledDeliveryDate'],
            'delivered_date': info['DocumentDeliveryDate'],
            'recipient_city': info['CityRecipient'],
            'recipient_name': info['RecipientFullName'],
            'afterpayment_cost': info['AfterpaymentOnGoodsCost']
        }
    else:
        return 'Wrong ttn'
