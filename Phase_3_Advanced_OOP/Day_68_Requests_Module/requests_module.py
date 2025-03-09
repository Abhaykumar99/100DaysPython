# ============================================================
# Day 68: Requests Module — Interacting with the Web
# ============================================================
# pip install requests
# ============================================================

import requests

# --- BASIC GET REQUEST ---
print("--- GET Request ---")
response = requests.get("https://httpbin.org/get")
print(f"Status Code : {response.status_code}")
print(f"Content-Type: {response.headers['Content-Type']}")
print(f"URL         : {response.url}")

# --- JSON RESPONSE ---
data = response.json()
print(f"Origin IP   : {data['origin']}")

# --- GET with PARAMETERS ---
print("\n--- GET with Parameters ---")
params = {"name": "Alice", "age": 22}
r = requests.get("https://httpbin.org/get", params=params)
print(f"Final URL: {r.url}")
print(f"Args    : {r.json()['args']}")

# --- POST REQUEST ---
print("\n--- POST Request ---")
payload = {"username": "alice", "password": "secret"}
r = requests.post("https://httpbin.org/post", json=payload)
print(f"Status  : {r.status_code}")
print(f"JSON sent: {r.json()['json']}")

# --- HEADERS ---
headers = {"User-Agent": "MyPythonApp/1.0", "Accept": "application/json"}
r = requests.get("https://httpbin.org/headers", headers=headers)
print(f"\nServer saw headers: {r.json()['headers']}")

# --- ERROR HANDLING ---
def safe_get(url, **kwargs):
    """Safe wrapper for requests.get."""
    try:
        r = requests.get(url, timeout=5, **kwargs)
        r.raise_for_status()    # Raises HTTPError for 4xx/5xx
        return r
    except requests.exceptions.ConnectionError:
        print("❌ Connection error!")
    except requests.exceptions.Timeout:
        print("❌ Request timed out!")
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error: {e}")
    return None

# Test 404
print("\n--- Error Handling ---")
r = safe_get("https://httpbin.org/status/404")
if r is None:
    print("Request failed safely.")

# --- USEFUL RESPONSE ATTRIBUTES ---
r = requests.get("https://httpbin.org/get")
print(f"\nr.status_code : {r.status_code}")
print(f"r.ok          : {r.ok}")
print(f"r.encoding    : {r.encoding}")
print(f"r.elapsed     : {r.elapsed.total_seconds():.3f}s")
# r.text  → response body as string
# r.json()→ parse JSON response
# r.content → raw bytes
