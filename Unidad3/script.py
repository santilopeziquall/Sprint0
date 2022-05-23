import json

# open json file and load its content to the variable data
with open("l3vpn.json") as json_file:
    data = json.load(json_file)

print("printing type of data...")
print(type(data))

print("\nprint data...")
print(data)

print("\nprint data in a nice json view...")
print(json.dumps(data, indent=2))

print("\nprint data['l3vpn'][0]['CustomerName']...")
print(data['l3vpn'][0]['CustomerName'])