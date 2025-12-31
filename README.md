# Binance Futures Order Bot (Demo / Testnet)

## Overview

This project is a command-line (CLI) based trading bot built in Python for Binance USDT-M Futures Demo (Testnet).

The bot allows users to place Market and Limit orders on Binance Futures using the official Binance API.  
It demonstrates API usage, input validation, logging, and clean project structure as part of a hiring assignment.

This project uses demo funds only and does not trade real money.

---

## Features

- Market Orders (BUY / SELL)
- Limit Orders (BUY / SELL)
- Binance Futures Demo/Testnet
- Command-line interface (CLI)
- Secure API key handling using .env
- Input validation (minimum notional check)
- Structured logging to bot.log
- Clean and reproducible project structure

---

## Project Structure

project_root/
│
├── src/
│ ├── market_orders.py
│ ├── limit_orders.py
│ └── advanced/
│ ├── oco.py
│ └── twap.py
│
├── bot.log
├── report.pdf
└── README.md

---

## Prerequisites

- Python 3.9 or higher
- Binance account
- Internet connection

---

## Setup Instructions

### 1. Install Python

Download Python from:
https://www.python.org

During installation, make sure “Add Python to PATH” is selected.

---

### 2. Install Required Libraries

Open a terminal in the project root and run:
python -m pip install python-binance python-dotenv

---

### 3. Create Binance Futures Demo Account

1. Go to https://testnet.binancefuture.com
2. Login using your Binance account
3. Ensure you are in DEMO TRADING mode
4. Verify demo USDT balance (around 10,000 USDT)

---

### 4. Create Demo Trading API Key

1. Click your profile icon
2. Select Demo Trading API
3. Create a new API key
4. Enable permissions:
   - Read
   - Trade
5. Copy the API Key and Secret Key

---

### 5. Create .env File

Create a file named .env in the project root with the following content:

BINANCE_API_KEY=your_demo_api_key_here
BINANCE_API_SECRET=your_demo_api_secret_here

Do not use quotes  
Do not commit .env to GitHub

---

## How to Run the Bot

### Market Order Example

python src/market_orders.py BTCUSDT BUY 0.002

### Limit Order Example

python src/limit_orders.py BTCUSDT SELL 0.002 95000

---

## Logs

All API requests, responses, and errors are logged in the bot.log file.

---

## Notes

- Binance Futures enforces a minimum notional value of 100 USDT
- Orders below this value will be rejected
- Demo/Testnet execution may differ slightly from real trading

---

## Disclaimer

This project is for educational and evaluation purposes only.  
It does not perform real trading or use real funds.
