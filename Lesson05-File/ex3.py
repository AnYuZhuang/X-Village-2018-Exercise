import json

new_data = [ { 'x' : 1, 'y' : 2, 'z' : 3, 'k' : 4, 'g' : 5 } ]

json = json.dumps(new_data)
print(json)