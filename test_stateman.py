# test_stateman.py
"""
Tests for StateMan module.
"""

import unittest
from stateman import StateMan

class TestStateMan(unittest.TestCase):
    """Test cases for StateMan class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = StateMan()
        self.assertIsInstance(instance, StateMan)
        
    def test_run_method(self):
        """Test the run method."""
        instance = StateMan()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
