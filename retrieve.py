"""
Created: 2023-10-23

retrieve.py
"""

import requests
import json
import sys
import io
import csv

# read API key for usage from locally stored ./.env file,
API_KEY = open(".env", 'r', encoding='utf-8').readline()
API_URL = 'https://www.alphavantage.co/query?'


# pull list of whitelisted tickers
tickercsv = open('tickers.csv', newline='')
reader = csv.reader(tickercsv, delimiter=',', quotechar='"')
tickers = reader.__next__()
tickercsv.close()


def summary_view(ticker):

    valid_ticker = False

    for x in range(len(tickers)):

        if ticker == tickers[x]:
            valid_ticker = True


    if not valid_ticker:

        print(ticker + " not in set of valid tickers")
        raise Exception('Invalid Ticker')

    r = requests.get(API_URL + 'function=OVERVIEW&symbol=' + ticker + "&apikey=" + API_KEY)
    data = r.json()

    print(data)


def detailed_view(ticker):
    pass


def daily_hist(ticker):
    pass


def weekly_hist(ticker):
    pass


def monthly_hist(ticker):
    pass


def yearly_hist(ticker):
    pass


def main(type, ticker):

    match type:
        case 's':
            summary_view(ticker)
        case 'd':
            detailed_view(ticker)
        case 'gd':
            daily_hist(ticker)
        case 'gw':
            weekly_hist(ticker)
        case 'gm':
            monthly_hist(ticker)
        case 'gy':
            yearly_hist(ticker)

if __name__ == "__main__":

    n = len(sys.argv)
    if (n != 3 ):
        raise Exception("Invalid amount of arguments")

    main(sys.argv[1], sys.argv[2])
