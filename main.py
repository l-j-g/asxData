import yfinance as yf
import pandas as pd
import csv
import yahoo_fin.stock_info as si
import os
tickers = []
with open('ASX_Listed_Companies_04-11-2021_04-29-57_AEDT.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)

for index, ticker in enumerate(data):
    tickers.append(f"{ticker[0]}.AX")

    
for ticker in tickers[1:5]:

    filename = f"./data/{ticker}/"
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    info = si.get_company_info(ticker)
    info['ticker'] = ticker
    info.to_csv(f"./data/{ticker}/{ticker}_info.csv",)

    valuation = si.get_stats_valuation(ticker)
    valuation['ticker'] = ticker
    valuation.to_csv(f"./data/{ticker}/{ticker}_valuation.csv")

    income_statement = si.get_income_statement(ticker)
    income_statement['ticker'] = ticker
    income_statement.to_csv(f"./data/{ticker}/{ticker}_income_statement.csv")

    balance_sheet = si.get_balance_sheet(ticker)
    balance_sheet['ticker'] = ticker
    balance_sheet.to_csv(f"./data/{ticker}/{ticker}_balance_sheet.csv")

    cash_flow = si.get_cash_flow(ticker)
    cash_flow['ticker'] = ticker
    cash_flow.to_csv(f"./data/{ticker}/{ticker}_cash_flow.csv")





