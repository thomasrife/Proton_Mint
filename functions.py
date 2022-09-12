from datetime import datetime

def timestamp_to_date(timestamp):
    dates = []
    for time in timestamp:
        dates.append(datetime.fromtimestamp(int(time, 0)).strftime('%d-%m-%y'))
        return dates

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