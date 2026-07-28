import streamlit as st
import pandas as pd

st.title("Portfolio Allocator")

st.info("Designed to help you choose the right portfolio")

capital = st.text_input("Enter investible capital")
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
  st.write("499")
with st.expander("Results of SQLSP"):
  st.write("779")

      
