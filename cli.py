#!/usr/bin/env python3
"""
Command-line interface for string diagonal traversal.
"""

import argparse
import sys
from string_diagonal import string_diagonal_transcribe, string_diagonal_transcribe_reverse, print_matrix


def main():
    parser = argparse.ArgumentParser(
        description="Transcribe strings using diagonal traversal patterns.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "HELLO"                    # Basic diagonal traversal
  %(prog)s "ABCDEFGHIJKL" -w 4        # Custom width
  %(prog)s "HELLO" --reverse          # Reverse diagonal
  %(prog)s "PROGRAMMING" --show-matrix # Show matrix visualization
        """
    )
    
    parser.add_argument(
        "text",
        help="Input string to transcribe"
    )
    
    parser.add_argument(
        "-w", "--width",
        type=int,
        help="Matrix width (default: auto-calculated square)"
    )
    
    parser.add_argument(
        "-r", "--reverse",
        action="store_true",
        help="Use reverse diagonal traversal (right-to-left)"
    )
    
    parser.add_argument(
        "-m", "--show-matrix",
        action="store_true",
        help="Show matrix visualization"
    )
    
    parser.add_argument(
        "-a", "--all",
        action="store_true",
        help="Show both forward and reverse traversals"
    )
    
    args = parser.parse_args()
    
    if not args.text:
        print("Error: Input text cannot be empty", file=sys.stderr)
        return 1
    
    # Show matrix if requested
    if args.show_matrix:
        print("Matrix visualization:")
        print_matrix(args.text, args.width)
        print()
    
    # Perform transcription
    if args.all:
        # Show both traversals
        forward = string_diagonal_transcribe(args.text, args.width)
        reverse = string_diagonal_transcribe_reverse(args.text, args.width)
        
        print(f"Original:        {args.text}")
        print(f"Forward (L->R):  {forward}")
        print(f"Reverse (R->L):  {reverse}")
        
    elif args.reverse:
        # Reverse diagonal only
        result = string_diagonal_transcribe_reverse(args.text, args.width)
        print(result)
        
    else:
        # Forward diagonal (default)
        result = string_diagonal_transcribe(args.text, args.width)
        print(result)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())