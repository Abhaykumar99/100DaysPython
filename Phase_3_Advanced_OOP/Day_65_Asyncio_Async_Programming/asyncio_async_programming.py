# ============================================================
# Day 65: asyncio Module — Asynchronous Programming
# ============================================================
# asyncio allows concurrent I/O without threads.
# async/await syntax to write non-blocking code.
# ============================================================

import asyncio
import time

# --- BASIC async function (coroutine) ---
async def say_hello():
    print("Hello!")
    await asyncio.sleep(1)    # Non-blocking sleep
    print("World!")

# Run a single coroutine
asyncio.run(say_hello())

# --- CONCURRENT TASKS ---
async def fetch_data(name, delay):
    """Simulate fetching data from an API."""
    print(f"⏳ {name}: Starting fetch...")
    await asyncio.sleep(delay)    # Non-blocking wait
    print(f"✅ {name}: Done in {delay}s!")
    return f"Data from {name}"

async def main():
    start = time.time()

    # Sequential (slow) — each task waits for the previous
    # result1 = await fetch_data("API_1", 2)
    # result2 = await fetch_data("API_2", 1)

    # Concurrent (fast) — all tasks run together
    results = await asyncio.gather(
        fetch_data("API_1", 2),
        fetch_data("API_2", 1),
        fetch_data("API_3", 3),
    )

    elapsed = time.time() - start
    print(f"\nAll done in {elapsed:.2f}s (max delay was 3s)")
    print("Results:", results)

print("\n--- Concurrent Tasks ---")
asyncio.run(main())

# --- ASYNC with tasks ---
async def task_demo():
    # Create tasks explicitly
    task1 = asyncio.create_task(fetch_data("Task_A", 1))
    task2 = asyncio.create_task(fetch_data("Task_B", 2))

    # Await them
    r1 = await task1
    r2 = await task2
    return r1, r2

print("\n--- Task Demo ---")
results = asyncio.run(task_demo())
print(results)

# --- KEY CONCEPTS ---
# async def    → defines a coroutine
# await        → pauses coroutine until awaited thing completes
# asyncio.run  → entry point; runs the event loop
# asyncio.gather → run multiple coroutines concurrently
# asyncio.create_task → schedule coroutine without waiting immediately
