# ============================================================
# Day 63: Function Caching using lru_cache
# ============================================================
# lru_cache (Least Recently Used) memoizes function results.
# Avoids redundant computation for same inputs.
# ============================================================

from functools import lru_cache
import time

# --- WITHOUT CACHE (slow) ---
def fib_slow(n):
    if n <= 1:
        return n
    return fib_slow(n-1) + fib_slow(n-2)

start = time.time()
print("fib(35) without cache:", fib_slow(35))
print(f"Time: {time.time() - start:.3f}s")

# --- WITH @lru_cache ---
@lru_cache(maxsize=128)   # Cache up to 128 unique calls
def fib_fast(n):
    if n <= 1:
        return n
    return fib_fast(n-1) + fib_fast(n-2)

start = time.time()
print("\nfib(35) with lru_cache:", fib_fast(35))
print(f"Time: {time.time() - start:.6f}s")

# Cache info
print(f"Cache info: {fib_fast.cache_info()}")

# Clear cache
fib_fast.cache_clear()
print(f"After clear: {fib_fast.cache_info()}")

# --- PRACTICAL: Memoizing expensive API-like calls ---
@lru_cache(maxsize=64)
def expensive_computation(n):
    """Simulates an expensive computation."""
    time.sleep(0.1)   # Simulate delay
    return n ** 3

print("\n--- Caching expensive calls ---")
for val in [5, 10, 5, 10, 5]:    # 5 and 10 will be cached after first call
    start = time.time()
    result = expensive_computation(val)
    elapsed = time.time() - start
    print(f"  expensive({val}) = {result} | time={elapsed:.4f}s")

print(f"\nFinal cache info: {expensive_computation.cache_info()}")

# --- functools.cache (Python 3.9+, unlimited cache) ---
from functools import cache

@cache
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

print(f"\n10! = {factorial(10)}")
print(f"Cache: {factorial.cache_info()}")
