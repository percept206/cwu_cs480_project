"""
Created: 2023-10-23

retrieve.py
"""

import requests
import json
import sys
import io
import csv

import parser_database
import parser_json
import database_manager

# read API key for usage from locally stored ./.env file,+
API_KEY = open(".env", 'r', encoding='utf-8').readline()
API_URL = 'https://www.alphavantage.co/query?'


# pull list of whitelisted tickers
tickercsv = open('tickers.csv', newline='')
reader = csv.reader(tickercsv, delimiter=',', quotechar='"')
tickers = reader.__next__()
tickercsv.close()

def print_tickers():
    print(tickers)


def db_populate_dailyHist():

    dbm = database_manager.DatabaseManager("financial_db.db")
    json_parser = parser_json.ParserJSON()
    db_parser = parser_database.ParserDB()

    for x in range(len(tickers)):
        cik = db_parser.ticker_to_cik(dbm, tickers[x])
        date = "2023-12-06"

        if db_parser.parse_from_daily_time_series(dbm, (cik, date)):
            continue

        r = requests.get(API_URL + 'function=TIME_SERIES_DAILY&symbol=' + tickers[x] + "&apikey=" + API_KEY) # each api call for each ticker
        data = r.json()
        parsedJSON = json_parser.parse_from_json(data)

        db_parser.parse_into_daily_time_series(dbm, (cik, date), parsedJSON)


def valid_ticker(ticker):
    valid_ticker = False

    for x in range(len(tickers)):

        if ticker == tickers[x]:
            valid_ticker = True

    return valid_ticker

def summary_view(ticker):

    if not valid_ticker(ticker): 

        print(ticker + " not in set of valid tickers")
        raise Exception('Invalid Ticker')

    r = requests.get(API_URL + 'function=OVERVIEW&symbol=' + ticker + "&apikey=" + API_KEY)
    data = r.json()

    values = []

    """
    this is a inefficient implementation 
    """
    values.append(float(data['52WeekHigh']))
    values.append(float(data['52WeekLow']))
    values.append(float(data['Beta']))
    values.append(float(data['PriceToBookRatio']))
    values.append(float(data['DividendPerShare']))
    values.append(float(data['DividendYield']))
    values.append(float(data['MarketCapitalization']))
    values.append(int(data['SharesOutstanding']))
    values.append(float(data['EPS']))
    values.append(float(data['QuarterlyEarningsGrowthYOY']))
    values.append(float(data['RevenuePerShareTTM']))
    values.append(float(data['RevenueTTM']))
    values.append(float(data['QuarterlyRevenueGrowthYOY']))
    values.append(float(data['EVToRevenue']))
    values.append(float(data['GrossProfitTTM']))
    values.append(float(data['PriceToSalesRatioTTM']))
    values.append(float(data['EBITDA']))
    values.append(float(data['EVToEBITDA']))
    values.append(float(data['ProfitMargin']))
    values.append(float(data['OperatingMarginTTM']))
    values.append(float(data['ReturnOnEquityTTM']))
    values.append(float(data['PERatio']))
    values.append(float(data['AnalystTargetPrice']))

    return values


def detailed_view(ticker):

    if not valid_ticker(ticker):
        print(ticker + " not in set of valid tickers")
        raise Exception('Invalid Ticker')


    r = requests.get(API_URL + 'function=INCOME_STATEMENT&symbol=' + ticker + "&apikey=" + API_KEY)
    income_statement = r.json()

    r = requests.get(API_URL + 'function=BALANCE_SHEET&symbol=' + ticker + "&apikey=" + API_KEY)
    balance_sheet = r.json()

    r = requests.get(API_URL + 'function=CASH_FLOW&symbol=' + ticker + "&apikey=" + API_KEY)
    cash_flow = r.json()

    details = (income_statement, balance_sheet, cash_flow)
    print("Income Statement: ", cash_flow)

def intraday_hist(ticker):

    if not valid_ticker(ticker):
        print(ticker + " not in set of valid tickers")
        raise Exception('Invalid Ticker')

    r = requests.get(API_URL + 'function=TIME_SERIES_INTRADAY&symbol=' + ticker + "&apikey=" + API_KEY)
    data = r.json()

    dates = []
    opens = []
    highs = []
    lows = []
    closes = []
    vol = []


    for date in data['Weekly Time Series']:
        dates.append(date)

    for value in data['Weekly Time Series'].values():
        opens.append(float(value['1. open']))
        highs.append(float(value['2. high']))
        lows.append(float(value['3. low']))
        closes.append(float(value['4. close']))
        vol.append((int(value['5. volume'])))

    intervals = [dates, opens, closes, lows, highs, vol]

    return intervals

def daily_hist(ticker):

    if not valid_ticker(ticker):
        print(ticker + " not in set of valid tickers")
        raise Exception('Invalid Ticker')

    r = requests.get(API_URL + 'function=TIME_SERIES_DAILY&symbol=' + ticker + "&apikey=" + API_KEY)
    data = r.json()

    dates = []
    opens = []
    highs = []
    lows = []
    closes = []
    vol = []


    for date in data['Time Series (Daily)']:
        dates.append(date)

    for value in data['Time Series (Daily)'].values():
        opens.append(float(value['1. open']))
        highs.append(float(value['2. high']))
        lows.append(float(value['3. low']))
        closes.append(float(value['4. close']))
        vol.append((int(value['5. volume'])))

    intervals = [dates, opens, closes, lows, highs, vol]

    return intervals

def weekly_hist(ticker):

    if not valid_ticker(ticker):
        print(ticker + " not in set of valid tickers")
        raise Exception('Invalid Ticker')

    r = requests.get(API_URL + 'function=TIME_SERIES_WEEKLY&symbol=' + ticker + "&apikey=" + API_KEY)
    data = r.json()

    dates = []
    opens = []
    highs = []
    lows = []
    closes = []
    vol = []


    for date in data['Weekly Time Series']:
        dates.append(date)

    for value in data['Weekly Time Series'].values():
        opens.append(float(value['1. open']))
        highs.append(float(value['2. high']))
        lows.append(float(value['3. low']))
        closes.append(float(value['4. close']))
        vol.append((int(value['5. volume'])))

    intervals = [dates, opens, closes, lows, highs, vol]

    return intervals


def monthly_hist(ticker):

    if not valid_ticker(ticker):
        print(ticker + " not in set of valid tickers")
        raise Exception('Invalid Ticker')


    r = requests.get(API_URL + 'function=TIME_SERIES_MONTHLY&symbol=' + ticker + "&apikey=" + API_KEY)
    data = r.json()

    dates = []
    opens = []
    highs = []
    lows = []
    closes = []
    vol = []


    print(data)
    for date in data['Monthly Time Series']:
        dates.append(date)

    for value in data['Monthly Time Series'].values():
        opens.append(float(value['1. open']))
        highs.append(float(value['2. high']))
        lows.append(float(value['3. low']))
        closes.append(float(value['4. close']))
        vol.append((int(value['5. volume'])))

    intervals = [dates, opens, closes, lows, highs, vol]

    print(dates)
    print(opens)
    print(highs)
    print(lows)
    print(closes)
    return intervals


def main(type, ticker):

    match type:
        case 's':
            summary_view(ticker)
        case 'd':
            detailed_view(ticker)
        case 'gi':
            intraday_hist(ticker)
        case 'gd':
            daily_hist(ticker)
        case 'gw':
            weekly_hist(ticker)
        case 'gm':
            monthly_hist(ticker)
        case 'db':
            db_populate_dailyHist()


if __name__ == "__main__":

    n = len(sys.argv)

    if (n == 2):
        if sys.argv[1] == "db":
            main(sys.argv[1], "")

    if (n != 3 ):
        raise Exception("Invalid amount of arguments")

    main(sys.argv[1], sys.argv[2])
