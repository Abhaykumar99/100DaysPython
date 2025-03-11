# ============================================================
# Day 70: Time Module — Execution Time & Delays
# ============================================================

import time
import datetime

# --- BASIC TIME FUNCTIONS ---
print(f"time.time()         : {time.time()}")          # Epoch seconds (float)
print(f"time.ctime()        : {time.ctime()}")          # Human-readable
print(f"time.localtime()    : {time.localtime()}")      # struct_time
print(f"time.gmtime()       : {time.gmtime()}")         # UTC struct_time

# --- FORMATTING TIME ---
t = time.localtime()
formatted = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(f"\nFormatted now       : {formatted}")

# Common format codes:
# %Y → 4-digit year    %m → month (01-12)   %d → day (01-31)
# %H → hour (00-23)    %M → minute (00-59)  %S → second (00-59)
# %A → weekday name    %B → month name      %p → AM/PM

# --- SLEEP ---
print("\nSleeping for 1 second...")
start = time.time()
time.sleep(1)
end   = time.time()
print(f"Slept for: {end - start:.3f}s")

# --- MEASURING EXECUTION TIME ---
def is_prime(n):
    if n < 2: return False
    return all(n % i != 0 for i in range(2, int(n**0.5)+1))

start = time.perf_counter()   # Higher precision than time.time()
primes = [n for n in range(2, 10000) if is_prime(n)]
end   = time.perf_counter()
print(f"\nFound {len(primes)} primes in {(end-start)*1000:.2f} ms")

# --- PROCESS TIME (CPU time only, not wall time) ---
cpu_start = time.process_time()
total = sum(i**2 for i in range(1_000_000))
cpu_end = time.process_time()
print(f"CPU time: {cpu_end - cpu_start:.3f}s")

# --- datetime module (more powerful for dates) ---
now = datetime.datetime.now()
print(f"\ndatetime.now()      : {now}")
print(f"now.year  = {now.year}")
print(f"now.month = {now.month}")
print(f"now.day   = {now.day}")

# Arithmetic
tomorrow = now + datetime.timedelta(days=1)
print(f"Tomorrow            : {tomorrow.date()}")

birthday   = datetime.date(1999, 8, 15)
today      = datetime.date.today()
age_days   = (today - birthday).days
print(f"Days since birthday : {age_days}")
