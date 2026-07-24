import streamlit as st
import pandas as pd


st.title("Portfolio Allocator")

st.info("Designed to help you choose the right portfolio")

capital = st.text_input("Enter investible capital")

