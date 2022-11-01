from pandas import read_csv
from statsmodels.tsa.arima.model import ARIMA
import numpy
from pandas import datetime
import requests
import json
from csv import writer
import time
import random

#Mobius addSlash
def addSlash(string):
    if string[0] != '/':
        string = '/' + string
    return string
#Mobius createContentInstance
def createContentInstance(AEname, dir, con, serverURL):
    dir = addSlash(dir)
    header = {
        "Accept": "application/json",
        "X-M2M-Origin": AEname,
        "X-M2M-RI": "12345",
        "Content-Type": "application/json;ty=4"
    }
    body = {
        "m2m:cin":{
            "con": con
        }
    }
    res = requests.post(serverURL+"/Mobius/"+AEname+dir, headers=header, json=body)
    print(res.json())

# create a differenced series
def difference(dataset, interval=1):
	diff = list()
	for i in range(interval, len(dataset)):
		value = dataset[i] - dataset[i - interval]
		diff.append(value)
	return numpy.array(diff)
 
# invert differenced value
def inverse_difference(history, yhat, interval=1):
	return yhat + history[-interval]

while(1):
    # load dataset
    series = read_csv("./scriptdata.csv", header=0)
    # seasonal difference
    X = series.values
    days_in_year = 365
    differenced = difference(X, days_in_year)
    # fit model
    model = ARIMA(differenced, order=(7,0,1))
    model_fit = model.fit()
    # one-step out of sample forecast
    start_index = len(differenced)
    end_index = len(differenced)
    forecast = model_fit.predict(start=start_index, end=end_index)
    # invert the differenced forecast to something usable
    forecast = inverse_difference(X, forecast, days_in_year)
    forecast = int(forecast)
    createContentInstance('ServiceUser', '/test', forecast, 'http://34.64.221.188:7579')
    print('Forecast: %d' % forecast)
    '''gen_random, modify
    series.iloc[500] = random.randint(forecast-2, forecast+2)
    series.to_csv("test.csv",index=False)
    forecast = [forecast]
    '''

    '''append
    forecast=[forecast]
    
    with open('dataset.csv','a',newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(forecast)
        f_object.close()
    '''
    time.sleep(2)
