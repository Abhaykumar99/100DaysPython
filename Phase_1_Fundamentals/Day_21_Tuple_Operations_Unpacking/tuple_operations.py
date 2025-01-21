# ============================================================
# Day 21: Tuple Operations & Unpacking
# ============================================================

# --- TUPLE CONCATENATION & REPETITION ---
t1 = (1, 2, 3)
t2 = (4, 5, 6)
print("Concat   :", t1 + t2)      # (1,2,3,4,5,6)
print("Repeat   :", t1 * 3)       # (1,2,3,1,2,3,1,2,3)

# --- TUPLE UNPACKING ---
point = (10, 20)
x, y = point
print(f"\nx = {x}, y = {y}")

rgb = (255, 128, 0)
red, green, blue = rgb
print(f"R={red}, G={green}, B={blue}")

# --- UNPACKING WITH * (star/splat) ---
first, *middle, last = (1, 2, 3, 4, 5)
print(f"\nFirst : {first}")
print(f"Middle: {middle}")   # list [2,3,4]
print(f"Last  : {last}")

# Swap two variables using tuple unpacking
a, b = 10, 20
print(f"\nBefore swap: a={a}, b={b}")
a, b = b, a
print(f"After swap : a={a}, b={b}")

# --- RETURNING MULTIPLE VALUES FROM FUNCTION ---
def divide(a, b):
    quotient  = a // b
    remainder = a % b
    return quotient, remainder    # returns a tuple

q, r = divide(17, 5)
print(f"\n17 ÷ 5 → quotient={q}, remainder={r}")

# --- TUPLE IN A LIST (records) ---
students = [
    ("Alice",  90, "A"),
    ("Bob",    75, "B"),
    ("Charlie", 60, "C"),
]
for name, marks, grade in students:
    print(f"{name:10} | {marks} | {grade}")
