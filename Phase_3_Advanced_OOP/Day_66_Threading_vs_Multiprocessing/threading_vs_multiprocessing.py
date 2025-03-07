# ============================================================
# Day 66: Multi-threading vs Multi-processing (Parallelism)
# ============================================================

import threading
import multiprocessing
import time

# ============================================================
# THREADING: Best for I/O-bound tasks (network, file ops)
# Threads share memory; GIL limits CPU parallelism in CPython.
# ============================================================

def download_file(name, duration):
    print(f"📥 [{threading.current_thread().name}] Downloading {name}...")
    time.sleep(duration)           # Simulate I/O wait
    print(f"✅ [{threading.current_thread().name}] {name} done!")

print("--- THREADING (I/O-bound) ---")
start = time.time()

threads = [
    threading.Thread(target=download_file, args=(f"file_{i}", 1), name=f"Thread-{i}")
    for i in range(1, 4)
]
for t in threads:
    t.start()
for t in threads:
    t.join()    # Wait for all threads to finish

print(f"Threading time: {time.time()-start:.2f}s\n")

# ============================================================
# MULTIPROCESSING: Best for CPU-bound tasks (computation)
# Each process has its own memory and Python interpreter.
# Bypasses the GIL!
# ============================================================

def cpu_task(n):
    """CPU-bound: compute sum of squares."""
    result = sum(i**2 for i in range(n))
    print(f"Process {multiprocessing.current_process().pid}: sum = {result}")

if __name__ == "__main__":
    print("--- MULTIPROCESSING (CPU-bound) ---")
    start = time.time()

    processes = [
        multiprocessing.Process(target=cpu_task, args=(500_000,))
        for _ in range(3)
    ]
    for p in processes:
        p.start()
    for p in processes:
        p.join()

    print(f"Multiprocessing time: {time.time()-start:.2f}s\n")

    # --- COMPARISON TABLE ---
    print("""
    | Feature      | Threading          | Multiprocessing    |
    |--------------|--------------------|--------------------|
    | Best for     | I/O-bound tasks    | CPU-bound tasks    |
    | Memory       | Shared memory      | Separate memory    |
    | GIL          | Limited by GIL     | Bypasses GIL       |
    | Overhead     | Low                | Higher             |
    | Complexity   | Moderate           | Higher             |
    | Safer?       | Race conditions    | More isolated      |
    """)
