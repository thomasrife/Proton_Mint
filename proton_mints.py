import requests
import pandas as pd
import json

url = "https://api.etherscan.io/api?module=logs&action=getLogs&fromBlock=11860010&toBlock=15210766&address=0x63174FA9680C674a5580f7d747832B2a2133Ad8f&topic0=0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef&&page=1&offset=1000&apikey=WGNWEA21FGPSPTHKGIG7A3IGBIXFBHJV2N"

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data={})
myjson = response.json()
ourdata = []

for x in myjson['result']:
    ourdata.append(x)

out_file = open("proton_mints.json", "w") 
    
json.dump(ourdata, out_file, indent = 4) 
    
out_file.close()

pdObj = pd.read_json('proton_mints.json')
pdObj.to_csv('proton_mints.csv', index=False)

print('done')