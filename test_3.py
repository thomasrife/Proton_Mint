from ntpath import join
from pydoc_data.topics import topics
from unittest import result
import requests
import pandas as pd
import json
from contract_events import dict_of_events

input_event = input("Event (Mint, Transfer, AproveForAll, SalePriceSet, UniverseSet, Test_4): ")
input_from_block = input("From Block: ")
input_to_block = input("To Block: ")
input_address = input("Address: ")
input_page = input("Page: ")
input_offset = input("Offset: ")
input_apikey = input("ApiKey: ")

query_http = "https://api.etherscan.io/api?module=logs&action=getLogs"
query_from_block = f"&fromBlock={input_from_block}"
querty_to_block = f"&toBlock={input_to_block}"
query_address = f"&address={input_address}"
query_page = f"&page={input_page}"
query_offset = f"&offset={input_offset}"
query_apikey = f"&apikey={input_apikey}"

input_event_values = list(dict_of_events[input_event].__dict__.values())

def url_maker(event_topics):
    
    url_start = query_http + query_from_block + querty_to_block + query_address
    url_ends = query_page + query_offset + query_apikey
    
    counter = 0
    topics = []
    for topic in event_topics:
        if topic != '':
            topics.append(f"&topic{counter}={event_topics[counter]}")
            counter += 1
    url_topic = ''.join(topics)
    return url_start + url_topic + url_ends

url = url_maker(input_event_values)

print(url)

