# Quantitative Portfolio Allocation System
An online portfolio allocator based on your risk appetite
Users can input their risk profile and the app will return what stocks they should invest in in what proportions such that it maximises sharpe ratio for their level of risk.

## How it works

The core logic lives in `port_man/portfolio_allocator.ipynb`. It:

1. Loads historical closing prices for 19 Indian large-cap stocks (Reliance, TCS, HDFC Bank, Infosys, and so on) from `stock_data_1.csv`.
2. Converts prices to log returns.
3. Runs a Monte Carlo simulation — 100,000 random portfolios — to map out the trade-off between return and volatility, and picks out the ones with the best Sharpe ratio and the lowest volatility.
4. Runs the same optimization properly using SLSQP (Sequential Least Squares Programming) from `scipy.optimize`, with weights constrained to sum to 100% and no shorting allowed.
5. Compares both approaches on Sharpe ratio, annual return, and volatility.

`port_man/streamlit_app.py` wraps this into a simple web app: enter how much capital you have, and it shows you the expected payout for two pre-computed portfolios (the Monte Carlo one and the SLSQP one).

## Running it

Install dependencies:

```bash
pip install -r port_man/requirements.txt
```

Open the notebook to see the full analysis:

```bash
jupyter notebook port_man/portfolio_allocator.ipynb
```

Or run the Streamlit app:

```bash
streamlit run port_man/streamlit_app.py
```

## Files

| File | What it is |
|---|---|
| `port_man/portfolio_allocator.ipynb` | Main notebook — data prep, Monte Carlo simulation, SLSQP optimization |
| `port_man/streamlit_app.py` | Web front-end for the two pre-computed portfolios |
| `stock_data_1.csv` | Historical price data for the 20 stocks |
| `port_man/requirements.txt` | Python dependencies |

## Notes

- Stock universe and pre-computed portfolio stats in the Streamlit app are currently hardcoded — the app doesn't run the optimizer live yet.
- One symbol's data failed to download, so the notebook works with 19 of the 20 stocks that are originally mentioned in the code.
- This is a student project, not investment advice.
