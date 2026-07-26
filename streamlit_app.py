import streamlit as st
import pandas as pd

st.title("Portfolio Allocator")

st.info("Designed to help you choose the right portfolio")

capital = st.text_input("Enter investible capital")
with st.expander("Stocks chosen for you"):
  st.write("💰Apple")
  st.write("💰Microsoft")
  st.write("💰SquarePoint Capital")

with st.expander("Details for max sharpe ratio"):
  st.write("53")
with st.expander("Details for min volatility"):
  st.write("779")

      
