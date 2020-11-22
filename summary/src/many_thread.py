import requests
import time
from concurrent.futures import *
from config import *


def get_url():
    requests.get(URL)

    
executor = ThreadPoolExecutor(max_workers=5)
futures = []
print(time.time())
for i in range(NUM):
    futures.append(executor.submit(get_url))
for future in futures:
    while not future.done():
        time.sleep(1)

print(time.time())