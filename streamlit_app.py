import streamlit as st
import pandas as pd


st.title("Portfolio Allocator")

st.info("Designed to help you choose the right portfolio")

capital = st.text_input("Enter investible capital")
with st.expander("Stocks chosen for you"):
  st.write("💰Apple")
  st.write("💰Microsoft")
  st.write("💰SquarePoint Capital")
  
from datetime import date
from datetime import datetime

import yfinance as yf

def get_price_history(symbols: List[str], start_date: str, end_date: str) -> pd.DataFrame:
    """
    Downloads historical stock prices from Yahoo Finance for multiple symbols
    and returns them in a single long-format DataFrame.

    Parameters
    ----------
    symbols : list
        List of ticker symbols.
    start_date : str
        Format: 'YYYY-MM-DD'
    end_date : str
        Format: 'YYYY-MM-DD'

    Returns
    -------
    pd.DataFrame
        DataFrame with 'Date', 'Symbol', and 'Close' (adjusted close) prices.
    """

    all_dfs = []

    for symbol in symbols:
        print(f"Downloading data for {symbol}...")
        df = yf.download(symbol,
                         start=start_date,
                         end=end_date,
                         auto_adjust=True, # Auto-adjust for splits and dividends
                         progress=False)

        if not df.empty:
            # Keep only 'Close' (which is adjusted close due to auto_adjust=True)
            # and rename to 'close' to match later pivot operation
            df_filtered = df[['Close']].copy()
            df_filtered.columns = ['close']
            df_filtered['symbol'] = symbol
            df_filtered['date'] = df_filtered.index # Make 'Date' a column
            df_filtered.reset_index(drop=True, inplace=True) # Reset index to be default integer index
            all_dfs.append(df_filtered)
            print(df_filtered.head())
        else:
            print(f"No data downloaded for {symbol}.")

        print("-" * 60)

    if all_dfs:
        combined_df = pd.concat(all_dfs, ignore_index=True)
        return combined_df
    else:
        return pd.DataFrame(columns=['date', 'symbol', 'close'])
      
