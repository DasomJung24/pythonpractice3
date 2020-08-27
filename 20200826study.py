import json
'''
customer = {
    'id': 152352,
    'name': '김철수',
    'history': [
        {'date': '2015-03-11', 'item': 'iPhone'},
        {'date': '2016-02-23', 'item': 'Monitor'},
    ]
}

jsonString = json.dumps(customer, indent=4)

print(jsonString)
print(type(jsonString))
'''

jsonString = '{"name": "김철수", "id": 152352, "history": [{"date": "2015-03-11", "item": "iPhone"}, {"date": "2016-02-23", "item": "Monitor"}]}'

dict = json.loads(jsonString)

print(dict['name'])
for h in dict['history']:
    print(h['date'], h['item'])