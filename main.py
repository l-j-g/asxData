import yfinance as yf
import pandas as pd
import csv
import yahoo_fin.stock_info as si
import os
tickers = []
with open('./ASX_Listed_Companies_07-02-2022_02-49-04_AEDT.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)

for index, ticker in enumerate(data):
    tickers.append(f"{ticker[0]}.AX")

count = 0    
for ticker in tickers[104:len(tickers)]:
    count += 1
    filename = f"./data/{ticker}/"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    try:
        info = si.get_company_info(ticker)
        info['ticker'] = ticker
        info.to_csv(f"./data/{ticker}/{ticker}_info.csv",)
    except:
        continue

    try:
        valuation = si.get_stats_valuation(ticker)
        valuation['ticker'] = ticker
        valuation.to_csv(f"./data/{ticker}/{ticker}_valuation.csv")
    except:
        continue
    try:
        income_statement = si.get_income_statement(ticker)
        income_statement['ticker'] = ticker
        income_statement.to_csv(f"./data/{ticker}/{ticker}_income_statement.csv")
    except:
        continue
    try:
        balance_sheet = si.get_balance_sheet(ticker)
        balance_sheet['ticker'] = ticker
        balance_sheet.to_csv(f"./data/{ticker}/{ticker}_balance_sheet.csv")
    except:
        continue
    try:
        cash_flow = si.get_cash_flow(ticker)
        cash_flow['ticker'] = ticker
        cash_flow.to_csv(f"./data/{ticker}/{ticker}_cash_flow.csv")
    except:
        continue
    print(f'Ticker: {ticker}, Count: {count}')




