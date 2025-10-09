"""Unit tests for the Stock Trading Portfolio system."""
import unittest
from datetime import datetime
from stock import Stock
from transaction import Transaction
from portfolio import Portfolio


class TestStock(unittest.TestCase):
    """Test cases for the Stock class."""
    
    def test_stock_creation(self):
        """Test creating a stock."""
        stock = Stock("AAPL", "Apple Inc.", 150.0)
        self.assertEqual(stock.symbol, "AAPL")
        self.assertEqual(stock.name, "Apple Inc.")
        self.assertEqual(stock.current_price, 150.0)
    
    def test_stock_symbol_uppercase(self):
        """Test that stock symbols are converted to uppercase."""
        stock = Stock("aapl", "Apple Inc.", 150.0)
        self.assertEqual(stock.symbol, "AAPL")
    
    def test_update_price(self):
        """Test updating stock price."""
        stock = Stock("AAPL", "Apple Inc.", 150.0)
        stock.update_price(160.0)
        self.assertEqual(stock.current_price, 160.0)
    
    def test_update_price_negative(self):
        """Test that negative price raises ValueError."""
        stock = Stock("AAPL", "Apple Inc.", 150.0)
        with self.assertRaises(ValueError):
            stock.update_price(-10.0)
    
    def test_stock_str(self):
        """Test string representation of stock."""
        stock = Stock("AAPL", "Apple Inc.", 150.0)
        self.assertEqual(str(stock), "AAPL (Apple Inc.): $150.00")
    
    def test_stock_repr(self):
        """Test repr of stock."""
        stock = Stock("AAPL", "Apple Inc.", 150.0)
        self.assertEqual(repr(stock), "Stock('AAPL', 'Apple Inc.', 150.0)")


class TestTransaction(unittest.TestCase):
    """Test cases for the Transaction class."""
    
    def test_buy_transaction(self):
        """Test creating a buy transaction."""
        transaction = Transaction("BUY", "AAPL", 10, 150.0)
        self.assertEqual(transaction.transaction_type, "BUY")
        self.assertEqual(transaction.symbol, "AAPL")
        self.assertEqual(transaction.shares, 10)
        self.assertEqual(transaction.price_per_share, 150.0)
        self.assertEqual(transaction.total_value, 1500.0)
    
    def test_sell_transaction(self):
        """Test creating a sell transaction."""
        transaction = Transaction("SELL", "AAPL", 5, 160.0)
        self.assertEqual(transaction.transaction_type, "SELL")
        self.assertEqual(transaction.total_value, 800.0)
    
    def test_invalid_transaction_type(self):
        """Test that invalid transaction type raises ValueError."""
        with self.assertRaises(ValueError):
            Transaction("HOLD", "AAPL", 10, 150.0)
    
    def test_invalid_shares(self):
        """Test that invalid shares raises ValueError."""
        with self.assertRaises(ValueError):
            Transaction("BUY", "AAPL", 0, 150.0)
        with self.assertRaises(ValueError):
            Transaction("BUY", "AAPL", -5, 150.0)
    
    def test_invalid_price(self):
        """Test that negative price raises ValueError."""
        with self.assertRaises(ValueError):
            Transaction("BUY", "AAPL", 10, -150.0)
    
    def test_transaction_timestamp(self):
        """Test transaction timestamp."""
        before = datetime.now()
        transaction = Transaction("BUY", "AAPL", 10, 150.0)
        after = datetime.now()
        self.assertTrue(before <= transaction.timestamp <= after)


class TestPortfolio(unittest.TestCase):
    """Test cases for the Portfolio class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.portfolio = Portfolio("Test Portfolio", 10000.0)
        self.apple = Stock("AAPL", "Apple Inc.", 150.0)
        self.tesla = Stock("TSLA", "Tesla Inc.", 250.0)
    
    def test_portfolio_creation(self):
        """Test creating a portfolio."""
        portfolio = Portfolio("My Portfolio", 5000.0)
        self.assertEqual(portfolio.name, "My Portfolio")
        self.assertEqual(portfolio.cash, 5000.0)
        self.assertEqual(len(portfolio.holdings), 0)
        self.assertEqual(len(portfolio.transactions), 0)
    
    def test_buy_stock(self):
        """Test buying stock."""
        result = self.portfolio.buy(self.apple, 10)
        self.assertTrue(result)
        self.assertEqual(self.portfolio.cash, 8500.0)
        self.assertIn("AAPL", self.portfolio.holdings)
        self.assertEqual(self.portfolio.holdings["AAPL"]["shares"], 10)
        self.assertEqual(len(self.portfolio.transactions), 1)
    
    def test_buy_insufficient_funds(self):
        """Test buying stock with insufficient funds."""
        result = self.portfolio.buy(self.apple, 100)
        self.assertFalse(result)
        self.assertEqual(self.portfolio.cash, 10000.0)
        self.assertNotIn("AAPL", self.portfolio.holdings)
    
    def test_buy_multiple_times(self):
        """Test buying same stock multiple times."""
        self.portfolio.buy(self.apple, 10)
        self.portfolio.buy(self.apple, 5)
        self.assertEqual(self.portfolio.holdings["AAPL"]["shares"], 15)
        self.assertEqual(len(self.portfolio.transactions), 2)
    
    def test_buy_invalid_shares(self):
        """Test buying with invalid shares."""
        with self.assertRaises(ValueError):
            self.portfolio.buy(self.apple, 0)
        with self.assertRaises(ValueError):
            self.portfolio.buy(self.apple, -5)
    
    def test_sell_stock(self):
        """Test selling stock."""
        self.portfolio.buy(self.apple, 10)
        result = self.portfolio.sell("AAPL", 5)
        self.assertTrue(result)
        self.assertEqual(self.portfolio.holdings["AAPL"]["shares"], 5)
        self.assertEqual(len(self.portfolio.transactions), 2)
    
    def test_sell_all_shares(self):
        """Test selling all shares removes holding."""
        self.portfolio.buy(self.apple, 10)
        result = self.portfolio.sell("AAPL", 10)
        self.assertTrue(result)
        self.assertNotIn("AAPL", self.portfolio.holdings)
    
    def test_sell_insufficient_shares(self):
        """Test selling more shares than owned."""
        self.portfolio.buy(self.apple, 10)
        result = self.portfolio.sell("AAPL", 15)
        self.assertFalse(result)
        self.assertEqual(self.portfolio.holdings["AAPL"]["shares"], 10)
    
    def test_sell_nonexistent_stock(self):
        """Test selling stock not in portfolio."""
        result = self.portfolio.sell("AAPL", 5)
        self.assertFalse(result)
    
    def test_sell_invalid_shares(self):
        """Test selling with invalid shares."""
        self.portfolio.buy(self.apple, 10)
        with self.assertRaises(ValueError):
            self.portfolio.sell("AAPL", 0)
        with self.assertRaises(ValueError):
            self.portfolio.sell("AAPL", -5)
    
    def test_get_value(self):
        """Test getting total portfolio value."""
        self.portfolio.buy(self.apple, 10)  # $1500
        self.portfolio.buy(self.tesla, 5)   # $1250
        # Cash remaining: 10000 - 1500 - 1250 = 7250
        # Total: 7250 + 1500 + 1250 = 10000
        self.assertEqual(self.portfolio.get_value(), 10000.0)
    
    def test_get_value_after_price_change(self):
        """Test getting value after stock price changes."""
        self.portfolio.buy(self.apple, 10)  # $1500
        self.apple.update_price(200.0)
        # Cash: 8500, Stock: 10 * 200 = 2000
        self.assertEqual(self.portfolio.get_value(), 10500.0)
    
    def test_get_holdings_summary(self):
        """Test getting holdings summary."""
        self.portfolio.buy(self.apple, 10)
        self.portfolio.buy(self.tesla, 5)
        summary = self.portfolio.get_holdings_summary()
        
        self.assertIn("AAPL", summary)
        self.assertEqual(summary["AAPL"]["shares"], 10)
        self.assertEqual(summary["AAPL"]["current_price"], 150.0)
        self.assertEqual(summary["AAPL"]["total_value"], 1500.0)
        
        self.assertIn("TSLA", summary)
        self.assertEqual(summary["TSLA"]["shares"], 5)
    
    def test_get_transaction_history(self):
        """Test getting transaction history."""
        self.portfolio.buy(self.apple, 10)
        self.portfolio.sell("AAPL", 5)
        history = self.portfolio.get_transaction_history()
        
        self.assertEqual(len(history), 2)
        self.assertEqual(history[0].transaction_type, "BUY")
        self.assertEqual(history[1].transaction_type, "SELL")
    
    def test_transaction_history_is_copy(self):
        """Test that transaction history returns a copy."""
        self.portfolio.buy(self.apple, 10)
        history1 = self.portfolio.get_transaction_history()
        self.portfolio.buy(self.tesla, 5)
        history2 = self.portfolio.get_transaction_history()
        
        self.assertEqual(len(history1), 1)
        self.assertEqual(len(history2), 2)


if __name__ == "__main__":
    unittest.main()
