"""Portfolio class to manage stock holdings."""
from transaction import Transaction
from stock import Stock


class Portfolio:
    """Manages a collection of stock holdings and transactions."""
    
    def __init__(self, name="My Portfolio", initial_cash=0.0):
        """
        Initialize a portfolio.
        
        Args:
            name (str): Portfolio name
            initial_cash (float): Starting cash balance
        """
        self.name = name
        self.cash = initial_cash
        self.holdings = {}  # {symbol: {'shares': int, 'stock': Stock}}
        self.transactions = []
    
    def buy(self, stock, shares):
        """
        Buy shares of a stock.
        
        Args:
            stock (Stock): Stock to buy
            shares (int): Number of shares to buy
            
        Returns:
            bool: True if purchase successful, False if insufficient funds
        """
        if shares <= 0:
            raise ValueError("Shares must be positive")
        
        cost = shares * stock.current_price
        
        if cost > self.cash:
            return False
        
        self.cash -= cost
        
        if stock.symbol in self.holdings:
            self.holdings[stock.symbol]['shares'] += shares
            self.holdings[stock.symbol]['stock'] = stock  # Update stock reference
        else:
            self.holdings[stock.symbol] = {'shares': shares, 'stock': stock}
        
        transaction = Transaction('BUY', stock.symbol, shares, stock.current_price)
        self.transactions.append(transaction)
        
        return True
    
    def sell(self, symbol, shares):
        """
        Sell shares of a stock.
        
        Args:
            symbol (str): Stock ticker symbol
            shares (int): Number of shares to sell
            
        Returns:
            bool: True if sale successful, False if insufficient shares
        """
        if shares <= 0:
            raise ValueError("Shares must be positive")
        
        symbol = symbol.upper()
        
        if symbol not in self.holdings or self.holdings[symbol]['shares'] < shares:
            return False
        
        stock = self.holdings[symbol]['stock']
        revenue = shares * stock.current_price
        self.cash += revenue
        
        self.holdings[symbol]['shares'] -= shares
        
        if self.holdings[symbol]['shares'] == 0:
            del self.holdings[symbol]
        
        transaction = Transaction('SELL', symbol, shares, stock.current_price)
        self.transactions.append(transaction)
        
        return True
    
    def get_value(self):
        """
        Calculate total portfolio value (cash + stock value).
        
        Returns:
            float: Total portfolio value
        """
        stock_value = sum(
            holding['shares'] * holding['stock'].current_price
            for holding in self.holdings.values()
        )
        return self.cash + stock_value
    
    def get_holdings_summary(self):
        """
        Get summary of current holdings.
        
        Returns:
            dict: Holdings summary with symbol as key
        """
        summary = {}
        for symbol, holding in self.holdings.items():
            stock = holding['stock']
            shares = holding['shares']
            current_value = shares * stock.current_price
            summary[symbol] = {
                'shares': shares,
                'current_price': stock.current_price,
                'total_value': current_value,
                'name': stock.name
            }
        return summary
    
    def get_transaction_history(self):
        """
        Get list of all transactions.
        
        Returns:
            list: List of Transaction objects
        """
        return self.transactions.copy()
    
    def __str__(self):
        """String representation of the portfolio."""
        holdings_str = "\n".join(
            f"  {symbol}: {holding['shares']} shares @ ${holding['stock'].current_price:.2f} = ${holding['shares'] * holding['stock'].current_price:.2f}"
            for symbol, holding in self.holdings.items()
        ) or "  (No holdings)"
        
        return (f"Portfolio: {self.name}\n"
                f"Cash: ${self.cash:.2f}\n"
                f"Holdings:\n{holdings_str}\n"
                f"Total Value: ${self.get_value():.2f}")
