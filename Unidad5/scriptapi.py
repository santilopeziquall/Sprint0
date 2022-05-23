import json
import requests
import json

def get_vendor(mac_address):
    url = "https://api.macvendors.com/"+mac_address
    r = requests.get(url)
    if r.status_code == 200:
        return r.text
    else:
        return r.status_code

hosts = {
    "192.168.0.4" : {"mac":"00:02:17:43:65:26"},
    "192.168.0.5" : {"mac":"14:5f:94:32:89:47"},
    "192.168.0.6" : {"mac":"00:14:F6:45:34:54"}
}

for key,value in hosts.items():
    vendor = get_vendor(value["mac"])
    hosts[key]["vendor"] = vendor

print("El resultado debajo debe ser Juniper Networks")
print(hosts["192.168.0.6"]["vendor"])

print("Todos los hosts con su vendor")
print(json.dumps(hosts, sort_keys=True, indent=4))

