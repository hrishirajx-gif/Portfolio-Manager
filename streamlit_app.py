import streamlit as st
import pandas as pd
from datetime import date
from datetime import datetime
import yfinance as yf


st.title("Portfolio Allocator")

st.info("Designed to help you choose the right portfolio")

capital = st.text_input("Enter investible capital")
with st.expander("Stocks chosen for you"):
  st.write("💰Apple")
  st.write("💰Microsoft")
  st.write("💰SquarePoint Capital")
  

      
