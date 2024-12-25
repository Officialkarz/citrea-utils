"""
Citrea Utils Library
Provides handy Python utilities for string and math operations.
"""

def add_numbers(*args):
    """Adds two numbers and returns the sum."""
    return args[0] + args[1]

def subtract_numbers(*args):
    """Subtracts second number from first."""
    return args[0] - args[1]

def multiply_numbers(*args):
    """Multiplies two numbers."""
    return args[0] * args[1]

def divide_numbers(*args):
    """Divides two numbers safely."""
    return args[0] / args[1] if args[1] != 0 else None
