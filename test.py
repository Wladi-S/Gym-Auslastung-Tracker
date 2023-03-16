import pandas as pd
import requests
import json
import csv
from datetime import datetime


nummer = 13

url = "https://portal.aidoo-online.de/workload"
parameter = {
    "mandant": "201900141_fitnesswerk_hassloch",
    "stud_nr": nummer,
    "jsonResponse": 1}

values_remove = ['gym', 'name', 'workload']


def getdata():
    response = requests.Session().get(url, params=parameter)
    data = response.json()
    data['time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    workload = data['numval']
    time = data['time']
    return time, workload


def get_data():
    response = requests.Session().get(url, params=parameter)
    data = response.json()
    for key in values_remove:
        data.pop(key)
    data['time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return data['numval']


print(getdata())


# with open('bellavitalis.txt', 'r') as text:
#   nummer = text.readlines()[0].split(',')
#  for element in nummer:
#     print(element)
