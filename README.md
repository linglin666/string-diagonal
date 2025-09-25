# String Diagonal Traversal

A Python implementation for transcribing strings using diagonal traversal patterns.

## Overview

This tool takes an input string, arranges it in a matrix format, and then reads it diagonally to create a transcribed version. This technique can be useful for string transformations, encoding, or pattern analysis.

## Features

- **Diagonal Traversal**: Read strings arranged in matrices using diagonal patterns
- **Two Traversal Modes**: 
  - Left-to-right diagonal traversal
  - Right-to-left diagonal traversal
- **Flexible Matrix Dimensions**: Specify custom width or use auto-calculated square dimensions
- **Visualization**: Helper function to display how strings are arranged in matrices

## Usage

### Basic Usage

```python
from string_diagonal import string_diagonal_transcribe

# Basic diagonal traversal
result = string_diagonal_transcribe("HELLO")
print(result)  # Output: HOELL

# With custom width
result = string_diagonal_transcribe("ABCDEFGHIJKL", width=4)
print(result)  # Output: AFKBGLCHDEJI
```

### Command Line Usage

```bash
# Run examples
python string_diagonal.py

# Run tests
python test_string_diagonal.py
```

### How It Works

1. **Matrix Creation**: The input string is arranged in a matrix with specified or calculated dimensions
2. **Diagonal Reading**: The matrix is traversed diagonally from top-left to bottom-right (or vice versa)
3. **Result Assembly**: Characters are collected in traversal order to form the transcribed string

### Example

For the string "HELLO" arranged in a 2x3 matrix:
```
H E L
L O  
```

Diagonal traversal (L->R) visits cells in this order: H → L → E → O → L
Result: "HOELL"

## API Reference

### `string_diagonal_transcribe(text, width=None)`

Transcribe a string using left-to-right diagonal traversal.

**Parameters:**
- `text` (str): Input string to transcribe
- `width` (int, optional): Matrix width. If None, uses square root of string length

**Returns:**
- `str`: Transcribed string

### `string_diagonal_transcribe_reverse(text, width=None)`

Transcribe a string using right-to-left diagonal traversal.

**Parameters:**
- `text` (str): Input string to transcribe  
- `width` (int, optional): Matrix width. If None, uses square root of string length

**Returns:**
- `str`: Transcribed string

### `print_matrix(text, width=None)`

Visualize how the string is arranged in the matrix.

**Parameters:**
- `text` (str): Input string
- `width` (int, optional): Matrix width

## Testing

Run the test suite to verify functionality:

```bash
python test_string_diagonal.py
```

The test suite includes:
- Empty string handling
- Single character inputs
- Square and rectangular matrices
- Custom width specifications
- Consistency validation (output contains same characters as input)

## Examples

```python
# Example 1: Basic usage
text = "PROGRAMMING"
result = string_diagonal_transcribe(text)
print(f"Original: {text}")
print(f"Transcribed: {result}")

# Example 2: Custom width
text = "ABCDEFGHIJKL"
result = string_diagonal_transcribe(text, width=4)
print(f"With width=4: {result}")

# Example 3: Reverse diagonal
text = "HELLO"
result = string_diagonal_transcribe_reverse(text)
print(f"Reverse diagonal: {result}")
```