import requests
import time


def session():

    headers = {'Cache-Control': 'no-cache', 'Connection': 'keep-alive'}
    client = requests.session()
    for i in range(200):
        time.sleep(1)
        response = client.get('http://8.131.82.49:82/admin/uploads/20201219_6081563259568567892.jpg',headers=headers)
        print("Status:", response.status_code)
        print("Content-type:", response.headers)


def no_session():

    headers = {'Cache-Control': 'no-cache', 'Connection': 'keep-alive'}
    for i in range(200):
        time.sleep(1)
        response = requests.get('http://8.131.82.49:82/admin/uploads/20201219_6081563259568567892.jpg',headers=headers)
        print("Status:", response.status_code)
        print("Content-type:", response.headers)


session()