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
        result = []
        for i in info['data']:
            date = i['DateCreated'].split(' ')[0].split('-')
            date = date.reverse()
            print(date)
            sent_date = '-'.join(date)
            date = i['ScheduledDeliveryDate'].split(' ')[0].split('-')
            date = date.reverse()
            schedule_date = '-'.join(date)
            result.append({
                'ttn': i['Number'],
                'status': i['Status'],
                'sent_date': sent_date,
                'schedule_date': schedule_date,
                'recipient_city': i['CityRecipient'],
                'recipient_name': i['RecipientFullName'],
                'afterpayment_cost': i['AfterpaymentOnGoodsCost']
            })
        return result
    else:
        return 'Wrong ttn'
