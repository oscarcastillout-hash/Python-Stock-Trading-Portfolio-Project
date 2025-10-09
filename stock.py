"""Stock class to represent individual stocks."""


class Stock:
    """Represents a stock with symbol and current price."""
    
    def __init__(self, symbol, name, current_price):
        """
        Initialize a stock.
        
        Args:
            symbol (str): Stock ticker symbol (e.g., 'AAPL')
            name (str): Company name
            current_price (float): Current price per share
        """
        self.symbol = symbol.upper()
        self.name = name
        self.current_price = current_price
    
    def update_price(self, new_price):
        """
        Update the current price of the stock.
        
        Args:
            new_price (float): New price per share
        """
        if new_price < 0:
            raise ValueError("Price cannot be negative")
        self.current_price = new_price
    
    def __str__(self):
        """String representation of the stock."""
        return f"{self.symbol} ({self.name}): ${self.current_price:.2f}"
    
    def __repr__(self):
        """Official string representation of the stock."""
        return f"Stock('{self.symbol}', '{self.name}', {self.current_price})"
