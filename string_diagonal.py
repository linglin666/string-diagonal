#!/usr/bin/env python3
"""
String Diagonal Traversal

This module provides functionality to transcribe strings using diagonal traversal.
The input string is arranged in a matrix format and then read diagonally.
"""

import math


def string_diagonal_transcribe(text, width=None):
    """
    Transcribe a string using diagonal traversal.
    
    Args:
        text (str): The input string to transcribe
        width (int, optional): Width of the matrix. If None, uses square root of length
        
    Returns:
        str: The transcribed string read diagonally
        
    Example:
        >>> string_diagonal_transcribe("HELLO")
        'HLOEL'
        >>> string_diagonal_transcribe("ABCDEFGHIJKL", 4)
        'AEIBFJCGKDHL'
    """
    if not text:
        return ""
    
    # Determine matrix dimensions
    if width is None:
        width = int(math.ceil(math.sqrt(len(text))))
    
    height = math.ceil(len(text) / width)
    
    # Create matrix and fill it with the text
    matrix = []
    text_index = 0
    
    for i in range(height):
        row = []
        for j in range(width):
            if text_index < len(text):
                row.append(text[text_index])
                text_index += 1
            else:
                row.append('')  # Empty cell for incomplete rows
        matrix.append(row)
    
    # Read diagonally
    result = []
    
    # Traverse upper-left to lower-right diagonals
    # Start from top row
    for start_col in range(width):
        row, col = 0, start_col
        while row < height and col < width:
            if matrix[row][col]:  # Skip empty cells
                result.append(matrix[row][col])
            row += 1
            col += 1
    
    # Start from left column (excluding top-left corner)
    for start_row in range(1, height):
        row, col = start_row, 0
        while row < height and col < width:
            if matrix[row][col]:  # Skip empty cells
                result.append(matrix[row][col])
            row += 1
            col += 1
    
    return ''.join(result)


def string_diagonal_transcribe_reverse(text, width=None):
    """
    Transcribe a string using reverse diagonal traversal (top-right to bottom-left).
    
    Args:
        text (str): The input string to transcribe
        width (int, optional): Width of the matrix. If None, uses square root of length
        
    Returns:
        str: The transcribed string read diagonally (reverse)
        
    Example:
        >>> string_diagonal_transcribe_reverse("HELLO")
        'EHLOL'
    """
    if not text:
        return ""
    
    # Determine matrix dimensions
    if width is None:
        width = int(math.ceil(math.sqrt(len(text))))
    
    height = math.ceil(len(text) / width)
    
    # Create matrix and fill it with the text
    matrix = []
    text_index = 0
    
    for i in range(height):
        row = []
        for j in range(width):
            if text_index < len(text):
                row.append(text[text_index])
                text_index += 1
            else:
                row.append('')  # Empty cell for incomplete rows
        matrix.append(row)
    
    # Read diagonally (reverse - top-right to bottom-left)
    result = []
    
    # Start from top row (right to left)
    for start_col in range(width - 1, -1, -1):
        row, col = 0, start_col
        while row < height and col >= 0:
            if matrix[row][col]:  # Skip empty cells
                result.append(matrix[row][col])
            row += 1
            col -= 1
    
    # Start from right column (excluding top-right corner)
    for start_row in range(1, height):
        row, col = start_row, width - 1
        while row < height and col >= 0:
            if matrix[row][col]:  # Skip empty cells
                result.append(matrix[row][col])
            row += 1
            col -= 1
    
    return ''.join(result)


def print_matrix(text, width=None):
    """
    Helper function to visualize how the string is arranged in the matrix.
    
    Args:
        text (str): The input string
        width (int, optional): Width of the matrix
    """
    if not text:
        print("Empty string")
        return
    
    if width is None:
        width = int(math.ceil(math.sqrt(len(text))))
    
    height = math.ceil(len(text) / width)
    
    print(f"Matrix ({height}x{width}):")
    text_index = 0
    
    for i in range(height):
        row = ""
        for j in range(width):
            if text_index < len(text):
                row += text[text_index] + " "
                text_index += 1
            else:
                row += "  "  # Empty space for incomplete rows
        print(row)


if __name__ == "__main__":
    # Demo examples
    test_strings = [
        "HELLO",
        "ABCDEFGHIJKL",
        "DIAGONAL",
        "PROGRAMMING"
    ]
    
    for text in test_strings:
        print(f"\nOriginal: {text}")
        print_matrix(text)
        transcribed = string_diagonal_transcribe(text)
        reverse_transcribed = string_diagonal_transcribe_reverse(text)
        print(f"Diagonal (L->R): {transcribed}")
        print(f"Diagonal (R->L): {reverse_transcribed}")