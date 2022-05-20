import requests
import json


response = requests.get(
    'https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=json&date=20220519&selectType=25&_=1653036695996')

# 使用json方法進行解析
print(response.json()['data'])
