# Python Stock Trading Portfolio Project

A Python-based stock trading portfolio management system that allows you to track stock holdings, execute buy/sell transactions, and monitor portfolio performance.

## Features

- **Stock Management**: Create and manage stock objects with ticker symbols, company names, and current prices
- **Portfolio Tracking**: Maintain a portfolio with cash balance and stock holdings
- **Buy/Sell Operations**: Execute buy and sell transactions with automatic cash and holdings updates
- **Transaction History**: Keep track of all buy and sell transactions with timestamps
- **Portfolio Valuation**: Calculate total portfolio value including cash and stock holdings
- **Price Updates**: Update stock prices and see real-time portfolio value changes

## Project Structure

```
├── stock.py           # Stock class for representing individual stocks
├── transaction.py     # Transaction class for tracking buy/sell operations
├── portfolio.py       # Portfolio class for managing stock holdings
├── example.py         # Example usage and demo script
├── test_portfolio.py  # Comprehensive unit tests
├── requirements.txt   # Project dependencies
└── README.md          # This file
```

## Installation

Clone the repository:
```bash
git clone https://github.com/oscarcastillout-hash/Python-Stock-Trading-Portfolio-Project.git
cd Python-Stock-Trading-Portfolio-Project
```

No external dependencies are required. The project uses only Python standard library (Python 3.6+).

## Usage

### Basic Example

```python
from stock import Stock
from portfolio import Portfolio

# Create a portfolio with initial cash
portfolio = Portfolio("My Portfolio", initial_cash=10000.0)

# Create stocks
apple = Stock("AAPL", "Apple Inc.", 150.00)
tesla = Stock("TSLA", "Tesla Inc.", 250.00)

# Buy stocks
portfolio.buy(apple, 20)  # Buy 20 shares of Apple
portfolio.buy(tesla, 10)  # Buy 10 shares of Tesla

# Check portfolio value
print(f"Total Portfolio Value: ${portfolio.get_value():.2f}")

# Update stock prices
apple.update_price(165.00)

# Sell stocks
portfolio.sell("AAPL", 10)  # Sell 10 shares of Apple

# View portfolio
print(portfolio)
```

### Running the Demo

Run the included example script to see the system in action:

```bash
python3 example.py
```

This will demonstrate:
- Creating a portfolio with initial cash
- Buying multiple stocks
- Simulating price changes
- Selling stocks
- Viewing transaction history
- Displaying holdings summary

## API Reference

### Stock Class

```python
Stock(symbol, name, current_price)
```

**Methods:**
- `update_price(new_price)`: Update the current stock price
- `__str__()`: Get string representation of the stock

### Transaction Class

```python
Transaction(transaction_type, symbol, shares, price_per_share, timestamp=None)
```

**Attributes:**
- `transaction_type`: 'BUY' or 'SELL'
- `symbol`: Stock ticker symbol
- `shares`: Number of shares
- `price_per_share`: Price per share at transaction time
- `timestamp`: Transaction timestamp (defaults to current time)
- `total_value`: Total transaction value

### Portfolio Class

```python
Portfolio(name="My Portfolio", initial_cash=0.0)
```

**Methods:**
- `buy(stock, shares)`: Buy shares of a stock (returns True if successful)
- `sell(symbol, shares)`: Sell shares of a stock (returns True if successful)
- `get_value()`: Get total portfolio value (cash + stock value)
- `get_holdings_summary()`: Get detailed summary of all holdings
- `get_transaction_history()`: Get list of all transactions
- `__str__()`: Get formatted portfolio summary

## Testing

Run the comprehensive test suite:

```bash
python3 -m unittest test_portfolio.py -v
```

The test suite includes 27 tests covering:
- Stock creation and price updates
- Transaction creation and validation
- Portfolio operations (buy/sell)
- Portfolio valuation
- Edge cases and error handling

## Example Output

```
============================================================
Stock Trading Portfolio Demo
============================================================

Created portfolio with $10000.00 initial cash

Available stocks:
  AAPL (Apple Inc.): $150.00
  GOOGL (Alphabet Inc.): $2800.00
  TSLA (Tesla Inc.): $250.00

Buying stocks...
  ✓ Bought 20 shares of AAPL
  ✓ Bought 10 shares of TSLA

Portfolio: My Investment Portfolio
Cash: $4500.00
Holdings:
  AAPL: 20 shares @ $150.00 = $3000.00
  TSLA: 10 shares @ $250.00 = $2500.00
Total Value: $10000.00
```

## Features and Capabilities

### Portfolio Management
- Track multiple stock holdings simultaneously
- Maintain cash balance with automatic updates
- Prevent buying with insufficient funds
- Prevent selling more shares than owned

### Transaction Tracking
- Record all buy and sell transactions
- Timestamp each transaction automatically
- Maintain complete transaction history
- Calculate transaction total values

### Price Management
- Update stock prices in real-time
- Portfolio value reflects current market prices
- Track gains and losses from price changes

### Data Validation
- Validate transaction types (BUY/SELL only)
- Ensure positive share quantities
- Prevent negative prices
- Convert stock symbols to uppercase automatically

## License

This project is open source and available for educational purposes.

## Contributing

Contributions are welcome! Feel free to submit issues and pull requests.