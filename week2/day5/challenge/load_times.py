import requests
import time

def get_load_time(url):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    
    load_time = end_time - start_time
    return load_time

# Tests
websites = ['https://www.google.com', 'https://www.ynet.co.il', 'https://www.imdb.com']
for site in websites:
    print(f"{site} took {get_load_time(site):.4f} seconds to load.")
