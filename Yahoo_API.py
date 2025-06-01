import yfinance as yf


aapl = yf.Ticker('AAPL')
#print(aapl.dividends)
#print(aapl.balance_sheet)
#balance_sheet_df = aapl.balance_sheet
#balance_sheet_df.to_excel('Apple_Data.xlsx')
#import ssl
#print(ssl.OPENSSL_VERSION)

dividend_df = aapl.dividends
dividend_df.index = dividend_df.index.tz_localize(None)
dividend_df.to_excel("Apple_Data.xlsx")
