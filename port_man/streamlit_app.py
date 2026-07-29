import streamlit as st
import pandas as pd

st.title("Portfolio Allocator")

st.info("Designed to help you choose the right portfolio")

capital = st.number_input("Enter investible capital in rupees")
with st.expander("Stocks chosen for you"):
  st.write("💰Bajaj Finance")
  st.write("💰BEL")
  st.write("💰Bharti Airtel")
  st.write("💰Dr. Reddys")
  st.write("💰HDFC Bank")
  st.write("💰Hindustan Unilever")
  st.write("💰ICICI Bank")
  st.write("💰Infosys")
  st.write("💰ITC")
  st.write("💰L&T")
  st.write("💰Mahindra & Mahindra")
  st.write("💰NTPC")
  st.write("💰Reliance")
  st.write("💰SBI Life")
  st.write("💰SBI")
  st.write("💰Sun Pharma")
  st.write("💰TCS")
  st.write("💰Titan")
  st.write("💰Ultratech Cement")


with st.expander("Results of Monte-Carlo Simulations"):
  st.write("Sharpe Ratio - 1.52838")
  st.write("Annual Returns - 21.5124%")
  st.write("Volatility - 14.0753%")
  st.write(f"In a year , this portfolio is expected to make you ₹ {0.215124*float(capital)} !")
with st.expander("Results of SQLSP"):
  st.write("Sharpe Ratio - 1.79528")
  st.write("Annual Returns -27.17707%")
  st.write("Volatility - 15.13806%")
  st.write(f"In a year , this portfolio is expected to make you ₹ {0.2717707*float(capital)} !")

