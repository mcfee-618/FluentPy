# coding:utf-8
import requests
import time
from config import *

print(time.time())
for i in range(NUM):
    response = requests.get(URL)
print(time.time())


