from unittest import result
import requests
import pandas as pd
import json

FromBlock = input("From Block: ")
ToBlock = input("To Block: ")
Address = input("Address: ")
Topic = input("Topic: ")
Topic_1 = input("Topic 1: ")
Page = input("Page: ")
Offset = input("Offset: ")
ApiKey = input("ApiKey: ")

def url_maker(fromBlock, toBlock, address, topic, page, offset, apiKey):
    if Topic_1 != "":
        url_query_1 = f"https://api.etherscan.io/api?module=logs&action=getLogs&fromBlock={fromBlock}&toBlock={toBlock}&address={address}&topic0={topic}&topic0_1_opr=and&topic1={Topic_1}&page={page}&offset={offset}&apikey={apiKey}"
        return url_query_1
    else:
        url_query_2 = f"https://api.etherscan.io/api?module=logs&action=getLogs&fromBlock={fromBlock}&toBlock={toBlock}&address={address}&topic0={topic}&topic0_1_opr=and&page={page}&offset={offset}&apikey={apiKey}"
        return url_query_2

url = url_maker(FromBlock, ToBlock, Address, Topic, Page, Offset, ApiKey)

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