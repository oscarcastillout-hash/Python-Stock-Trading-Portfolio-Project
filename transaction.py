"""Transaction class to track buy/sell operations."""
from datetime import datetime


class Transaction:
    """Represents a stock transaction (buy or sell)."""
    
    def __init__(self, transaction_type, symbol, shares, price_per_share, timestamp=None):
        """
        Initialize a transaction.
        
        Args:
            transaction_type (str): 'BUY' or 'SELL'
            symbol (str): Stock ticker symbol
            shares (int): Number of shares
            price_per_share (float): Price per share at transaction time
            timestamp (datetime, optional): Transaction timestamp. Defaults to current time.
        """
        if transaction_type.upper() not in ['BUY', 'SELL']:
            raise ValueError("Transaction type must be 'BUY' or 'SELL'")
        if shares <= 0:
            raise ValueError("Shares must be positive")
        if price_per_share < 0:
            raise ValueError("Price per share cannot be negative")
        
        self.transaction_type = transaction_type.upper()
        self.symbol = symbol.upper()
        self.shares = shares
        self.price_per_share = price_per_share
        self.timestamp = timestamp or datetime.now()
        self.total_value = shares * price_per_share
    
    def __str__(self):
        """String representation of the transaction."""
        return (f"{self.transaction_type} {self.shares} shares of {self.symbol} "
                f"at ${self.price_per_share:.2f} on {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
    
    def __repr__(self):
        """Official string representation of the transaction."""
        return (f"Transaction('{self.transaction_type}', '{self.symbol}', "
                f"{self.shares}, {self.price_per_share}, {self.timestamp})")
