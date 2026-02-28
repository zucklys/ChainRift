# test_chainrift.py
"""
Tests for ChainRift module.
"""

import unittest
from chainrift import ChainRift

class TestChainRift(unittest.TestCase):
    """Test cases for ChainRift class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ChainRift()
        self.assertIsInstance(instance, ChainRift)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ChainRift()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
