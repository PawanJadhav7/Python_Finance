# import yfinance as yf


# aapl = yf.Ticker('AAPL')
#print(aapl.dividends)
#print(aapl.balance_sheet)
#balance_sheet_df = aapl.balance_sheet
#balance_sheet_df.to_excel('Apple_Data.xlsx')
#import ssl
#print(ssl.OPENSSL_VERSION)

# dividend_df = aapl.dividends
# dividend_df.index = dividend_df.index.tz_localize(None)
# dividend_df.to_excel("Apple_Data.xlsx")


import certifi
import json
# url = "https://financialmodelingprep.com/stable/profile?symbol=AAPL&apikey=i8gyb6VbPSacCdyK0GOwZrQLqaxNudaA"
#!/usr/bin/env python
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen


def get_jsonparsed_data(url):
    response = urlopen(url, cafile=certifi.where())
    data = response.read().decode("utf-8")
    return json.loads(data)

url = ("https://financialmodelingprep.com/stable/income-statement?symbol=AAPL&apikey=i8gyb6VbPSacCdyK0GOwZrQLqaxNudaA")
# print(get_jsonparsed_data(url))
IncomeStatement_APPL = get_jsonparsed_data(url)
# print(IncomeStatement_APPL[0]['operatingExpenses'])

netIncomeRatios_APPL = []
# IncomeStatement_APPL[0]['operatingExpenses']['netIncomeRatio']
for i in range(0,5):
    netIncomeRatios_APPL.append(IncomeStatement_APPL[i]['netIncome'])
print(netIncomeRatios_APPL)