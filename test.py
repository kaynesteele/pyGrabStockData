import requests
import json
import sys
import time


f=open('watch.txt', 'r')

dat=f.readlines()


for x in dat:
    ticker=x.rstrip('\n')
    print(ticker)
    r=requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+ticker+'&apikey=SKY4KTW3LNI1DD7K')
    data=json.loads(r.text)
    outFile=open(ticker+".txt", "w")
    for i in data['Time Series (Daily)']:
        print(data['Time Series (Daily)'][i]['4. close'])
        outFile.write(data['Time Series (Daily)'][i]['4. close'] + "\n")
    time.sleep(15)

