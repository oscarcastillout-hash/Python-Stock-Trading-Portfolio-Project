"""Example usage of the Stock Trading Portfolio system."""
from stock import Stock
from portfolio import Portfolio


def main():
    """Demonstrate the stock trading portfolio functionality."""
    print("=" * 60)
    print("Stock Trading Portfolio Demo")
    print("=" * 60)
    print()
    
    # Create a portfolio with initial cash
    portfolio = Portfolio("My Investment Portfolio", initial_cash=10000.0)
    print(f"Created portfolio with ${portfolio.cash:.2f} initial cash")
    print()
    
    # Create some stocks
    apple = Stock("AAPL", "Apple Inc.", 150.00)
    google = Stock("GOOGL", "Alphabet Inc.", 2800.00)
    tesla = Stock("TSLA", "Tesla Inc.", 250.00)
    
    print("Available stocks:")
    print(f"  {apple}")
    print(f"  {google}")
    print(f"  {tesla}")
    print()
    
    # Buy some stocks
    print("Buying stocks...")
    if portfolio.buy(apple, 20):
        print(f"  ✓ Bought 20 shares of {apple.symbol}")
    if portfolio.buy(tesla, 10):
        print(f"  ✓ Bought 10 shares of {tesla.symbol}")
    if portfolio.buy(google, 2):
        print(f"  ✓ Bought 2 shares of {google.symbol}")
    print()
    
    # Display portfolio
    print(portfolio)
    print()
    
    # Simulate price changes
    print("Simulating market changes...")
    apple.update_price(165.00)
    tesla.update_price(280.00)
    google.update_price(2900.00)
    print(f"  {apple.symbol}: ${apple.current_price:.2f} (+10%)")
    print(f"  {tesla.symbol}: ${tesla.current_price:.2f} (+12%)")
    print(f"  {google.symbol}: ${google.current_price:.2f} (+3.6%)")
    print()
    
    # Display updated portfolio
    print("Portfolio after price changes:")
    print(portfolio)
    print()
    
    # Sell some stocks
    print("Selling stocks...")
    if portfolio.sell("TSLA", 5):
        print(f"  ✓ Sold 5 shares of TSLA")
    print()
    
    # Final portfolio status
    print("Final Portfolio Status:")
    print(portfolio)
    print()
    
    # Show transaction history
    print("Transaction History:")
    for i, transaction in enumerate(portfolio.get_transaction_history(), 1):
        print(f"  {i}. {transaction}")
    print()
    
    # Show holdings summary
    print("Holdings Summary:")
    summary = portfolio.get_holdings_summary()
    for symbol, info in summary.items():
        print(f"  {symbol} ({info['name']}):")
        print(f"    Shares: {info['shares']}")
        print(f"    Current Price: ${info['current_price']:.2f}")
        print(f"    Total Value: ${info['total_value']:.2f}")
    print()
    
    print("=" * 60)
    print("Demo Complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
