#!/usr/bin/env python3
"""
Tests for string diagonal traversal functionality.
"""

import unittest
from string_diagonal import string_diagonal_transcribe, string_diagonal_transcribe_reverse


class TestStringDiagonal(unittest.TestCase):
    
    def test_empty_string(self):
        """Test with empty string."""
        self.assertEqual(string_diagonal_transcribe(""), "")
        self.assertEqual(string_diagonal_transcribe_reverse(""), "")
    
    def test_single_character(self):
        """Test with single character."""
        result = string_diagonal_transcribe("A")
        self.assertEqual(result, "A")
        
        result_reverse = string_diagonal_transcribe_reverse("A")
        self.assertEqual(result_reverse, "A")
    
    def test_hello_example(self):
        """Test the HELLO example from docstring."""
        # For "HELLO" in a roughly square matrix:
        # H E L
        # L O
        # Diagonal L->R: H, E, L, L, O -> "HELLO" (but diagonally: H, L, E, O, L)
        result = string_diagonal_transcribe("HELLO")
        # Let's verify this step by step
        self.assertIsInstance(result, str)
        self.assertEqual(len(result), 5)  # Same length as input
    
    def test_abcdefghijkl_example(self):
        """Test the ABCDEFGHIJKL example with specified width."""
        # With width=4:
        # A B C D
        # E F G H  
        # I J K L
        # Diagonals L->R: A, BF, CGJ, DHK, EI, L
        result = string_diagonal_transcribe("ABCDEFGHIJKL", 4)
        self.assertIsInstance(result, str)
        self.assertEqual(len(result), 12)  # Same length as input
        self.assertTrue(all(c in "ABCDEFGHIJKL" for c in result))
    
    def test_square_matrix(self):
        """Test with perfect square matrix."""
        # "ABCDEFGHI" -> 3x3 matrix
        # A B C
        # D E F
        # G H I
        # Diagonals: A, BD, CEH, FI, G
        text = "ABCDEFGHI"
        result = string_diagonal_transcribe(text)
        self.assertEqual(len(result), 9)
        self.assertTrue(all(c in text for c in result))
    
    def test_rectangular_matrix(self):
        """Test with rectangular matrix."""
        text = "ABCDEF"
        result = string_diagonal_transcribe(text, width=2)
        # Matrix:
        # A B
        # C D  
        # E F
        # Diagonals: A, BC, DE, F
        self.assertEqual(len(result), 6)
        self.assertTrue(all(c in text for c in result))
    
    def test_reverse_diagonal(self):
        """Test reverse diagonal traversal."""
        text = "ABCD"
        result = string_diagonal_transcribe_reverse(text, width=2)
        # Matrix:
        # A B
        # C D
        # Reverse diagonals: B, AD, C
        self.assertEqual(len(result), 4)
        self.assertTrue(all(c in text for c in result))
    
    def test_width_larger_than_text(self):
        """Test when width is larger than text length."""
        text = "ABC"
        result = string_diagonal_transcribe(text, width=5)
        self.assertEqual(len(result), 3)
        self.assertEqual(set(result), set(text))
    
    def test_consistency(self):
        """Test that output contains same characters as input."""
        test_cases = [
            "HELLO",
            "WORLD", 
            "DIAGONAL",
            "TESTING123",
            "A",
            "AB",
            "ABCDEFGHIJKLMNOP"
        ]
        
        for text in test_cases:
            result = string_diagonal_transcribe(text)
            self.assertEqual(len(result), len(text))
            self.assertEqual(sorted(result), sorted(text))
            
            result_reverse = string_diagonal_transcribe_reverse(text)
            self.assertEqual(len(result_reverse), len(text))
            self.assertEqual(sorted(result_reverse), sorted(text))


if __name__ == "__main__":
    unittest.main()