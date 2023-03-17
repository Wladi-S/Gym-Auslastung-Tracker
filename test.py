import pandas as pd
import requests
import json
import csv
from datetime import datetime


values_remove = ['gym', 'name', 'workload']


def get_data(nummer):
    """Datenabfrage der Auslastung des jeweiligen Gyms"""

    url = "https://portal.aidoo-online.de/workload"
    parameter = {
        "mandant": "201900141_fitnesswerk_hassloch",
        "stud_nr": nummer,
        "jsonResponse": 1}
    response = requests.Session().get(url, params=parameter).json()
    return response


for i in range(100, 200):
    print(i)
    print(get_data(i))


# with open('bellavitalis.txt', 'r') as text:
#   nummer = text.readlines()[0].split(',')
#  for element in nummer:
#     print(element)
