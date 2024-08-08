import yfinance as yf
import toml as tml
from datetime import date

def data_store_info(ticker):
    stock = yf.Ticker(f"{ticker}")
    stock_info = stock.info
    with open(f"datastore/{ticker}_info_{date.today()}.toml", "w") as file:
        tml.dump(stock_info, file)

        file.close()


data_store_info("MSFT")
