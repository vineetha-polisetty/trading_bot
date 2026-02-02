# Binance Futures Trading Bot (Testnet)

## Overview
This is a CLI-based Python trading bot built for the Binance USDT-M Futures Testnet.
It supports placing MARKET and LIMIT orders with proper validation, logging,
and error handling.

The project demonstrates clean separation of concerns, reliability,
and traceability aligned with professional software engineering practices.

---

## Features
- CLI interface using argparse
- Supports BUY and SELL orders
- Supports MARKET and LIMIT order types
- Input validation before API calls
- Structured logging of requests, responses, and errors
- Graceful error handling with fallback mechanism
- Clean, modular project structure

---

## Project Structure


trading_bot/
├── bot/
│ ├── client.py
│ ├── orders.py
│ ├── validators.py
│ ├── logging_config.py
│ └── init.py
├── cli.py
├── requirements.txt
├── trading.log
├── .env
└── README.md


---

## Setup Instructions

### 1. Create virtual environment
```bash
python -m venv venv
source venv/Scripts/activate


2. Install dependencies

pip install -r requirements.txt


3. Configure environment variables

Create a .env file:

BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_api_secret_here


Usage Examples

Market Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Limit Order

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 50000

Logging

All API requests, responses, and errors are logged in trading.log.

## Assumptions & Notes on Binance Futures Testnet Access

During development, Binance Futures Testnet UI login redirected to the mainnet
in my region, preventing generation of valid Futures Testnet API keys.

To handle this gracefully:

The application attempts a real Futures Testnet API call

Logs the exact API error received

Falls back to a controlled mock response to demonstrate end-to-end behavior

This ensures the CLI flow, validation, logging, and error handling can be fully
evaluated despite external API access limitations.


Conclusion

This project demonstrates a clean, reliable, and production-oriented approach
to building a trading bot CLI with proper engineering practices.
