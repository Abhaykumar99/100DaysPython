# ============================================================
# Day 25: Recursion — Factorials & Fibonacci
# ============================================================
# Recursion: a function that calls itself.
# Every recursive function needs a BASE CASE to stop.
# ============================================================

# --- FACTORIAL using Recursion ---
# 5! = 5 × 4 × 3 × 2 × 1 = 120
# Base case: 0! = 1  or  1! = 1

def factorial(n):
    """Return the factorial of n using recursion."""
    if n <= 1:         # BASE CASE
        return 1
    return n * factorial(n - 1)   # RECURSIVE CALL

print("Factorial Examples:")
for i in range(0, 11):
    print(f"  {i}! = {factorial(i)}")

# --- FIBONACCI using Recursion ---
# Series: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# fib(n) = fib(n-1) + fib(n-2)
# Base cases: fib(0)=0, fib(1)=1

def fibonacci(n):
    """Return the nth Fibonacci number using recursion."""
    if n == 0:         # BASE CASE
        return 0
    if n == 1:         # BASE CASE
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print("\nFibonacci Series (first 10):")
print([fibonacci(i) for i in range(10)])

# --- POWER using Recursion ---
def power(base, exp):
    """Return base raised to exp using recursion."""
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

print(f"\n2^10 = {power(2, 10)}")

# --- ⚠️ RECURSION PITFALLS ---
# 1. Always have a base case (else → infinite recursion → RecursionError)
# 2. Python's default recursion limit is 1000
import sys
print(f"\nRecursion limit: {sys.getrecursionlimit()}")

# --- TIP: Iterative vs Recursive ---
# Recursion is elegant but can be slower due to function call overhead.
# For Fibonacci, iterative or memoization is preferred for large n.

def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print(f"\nfib(30) iterative  = {fibonacci_iterative(30)}")
print(f"fib(30) recursive  = {fibonacci(30)}")
