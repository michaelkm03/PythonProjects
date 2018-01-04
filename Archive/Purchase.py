import json

file = 'staging-purchase-user-status (1).csv'
h = open(file)
text = h.read()
json = json.dumps(text)

#for i in json: