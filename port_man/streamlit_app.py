import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns

st.title("Portfolio Allocator")
st.info("Designed to help you choose the right portfolio")

capital = st.text_input("Enter investible capital")

# Your 19 stocks, in the SAME order as your `symbols` list / optimized_sharpe.x
stock_names = [
    "Bajaj Finance", "BEL", "Bharti Airtel", "Dr. Reddys", "HDFC Bank",
    "Hindustan Unilever", "ICICI Bank", "Infosys", "ITC", "L&T",
    "Mahindra & Mahindra", "NTPC", "Reliance", "SBI Life", "SBI",
    "Sun Pharma", "TCS", "Titan", "Ultratech Cement"
]

with st.expander("Stocks chosen for you"):
    for name in stock_names:
        st.write(f"💰{name}")

with st.expander("Results of Monte-Carlo Simulations"):
    st.write("499")

with st.expander("Results of SQLSP"):
    st.write("779")

# ---- Heatmap section ----
def plot_portfolio_heatmap(names, weights, capital, ncols=5):
    weights = np.array(weights, dtype=float)
    amounts = weights * capital

    # add the 20th box for total portfolio
    all_names = names + ["TOTAL\nPORTFOLIO"]
    all_weights = np.append(weights, weights.sum())
    all_amounts = np.append(amounts, amounts.sum())

    nrows = int(np.ceil(len(all_names) / ncols))
    pad = nrows * ncols - len(all_names)
    if pad > 0:
        all_names += [""] * pad
        all_weights = np.append(all_weights, [np.nan] * pad)
        all_amounts = np.append(all_amounts, [np.nan] * pad)

    z = all_weights.reshape(nrows, ncols)
    name_grid = np.array(all_names).reshape(nrows, ncols)
    amt_grid = all_amounts.reshape(nrows, ncols)

    labels = np.empty((nrows, ncols), dtype=object)
    for i in range(nrows):
        for j in range(ncols):
            n = name_grid[i, j]
            labels[i, j] = "" if n == "" else f"{n}\n{z[i,j]*100:.1f}%\n₹{amt_grid[i,j]:,.0f}"

    fig, ax = plt.subplots(figsize=(ncols * 2.3, nrows * 1.9))
    sns.heatmap(
        z, annot=labels, fmt="", cmap="YlOrRd",
        linewidths=2, linecolor="white",
        mask=np.isnan(z), cbar_kws={"label": "Weight"},
        annot_kws={"size": 8}, xticklabels=False, yticklabels=False, ax=ax
    )
    ax.set_title("Portfolio Allocation Heatmap")
    fig.tight_layout()
    return fig


# weights = optimized_sharpe.x  <- from your SLSQP block, in the same order as stock_names

if capital:
    try:
        capital_value = float(capital)
        with st.expander("Portfolio Heatmap"):
            fig = plot_portfolio_heatmap(stock_names, weights, capital_value)
            st.pyplot(fig)
    except ValueError:
        st.error("Please enter a valid number for capital.")
