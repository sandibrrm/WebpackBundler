# test_webpackbundler.py
"""
Tests for WebpackBundler module.
"""

import unittest
from webpackbundler import WebpackBundler

class TestWebpackBundler(unittest.TestCase):
    """Test cases for WebpackBundler class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = WebpackBundler()
        self.assertIsInstance(instance, WebpackBundler)
        
    def test_run_method(self):
        """Test the run method."""
        instance = WebpackBundler()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
