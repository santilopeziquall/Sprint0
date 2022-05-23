import json

# open json file and load its content to the variable data
with open("l3vpn.json") as json_file:
    data = json.load(json_file)
# Define the message that corresponds to the status code
status_message = {"0":"Enable VPN", "1":"Disable VPN", "2":"Delete VPN"}

for customer in data["l3vpn"]:
    print(status_message[customer['Status']])
    print(customer['CustomerName'] + "\n")