# ============================================================
# Day 19: List Methods
# ============================================================
# append, insert, extend, remove, pop, sort, reverse, index, count
# ============================================================

nums = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# append() → add to end
nums.append(7)
print("append(7)    :", nums)

# insert(index, value) → add at specific position
nums.insert(0, 0)
print("insert(0,0)  :", nums)

# extend() → add all elements from another list
nums.extend([10, 11])
print("extend()     :", nums)

# remove() → remove first occurrence of value
nums.remove(1)
print("remove(1)    :", nums)

# pop() → remove and return element (default: last)
popped = nums.pop()
print(f"pop()        : removed {popped}, list = {nums}")

popped2 = nums.pop(0)
print(f"pop(0)       : removed {popped2}, list = {nums}")

# sort() → sort in place (ascending by default)
nums.sort()
print("sort()       :", nums)

# sort(reverse=True) → descending
nums.sort(reverse=True)
print("sort(desc)   :", nums)

# reverse() → reverse the list in place
nums.reverse()
print("reverse()    :", nums)

# index() → find index of first occurrence
print("\nindex(5)     :", nums.index(5))

# count() → count occurrences
nums2 = [1, 2, 2, 3, 2, 4]
print("count(2)     :", nums2.count(2))

# copy() & clear()
backup = nums.copy()
print("copy()       :", backup)

# List Comprehension (bonus preview!)
squares = [x**2 for x in range(1, 6)]
print("\nSquares 1-5  :", squares)
evens   = [x for x in range(1, 21) if x % 2 == 0]
print("Evens 1-20   :", evens)
