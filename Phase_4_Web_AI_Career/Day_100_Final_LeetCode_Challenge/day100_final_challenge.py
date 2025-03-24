# ============================================================
# Day 100: Final Challenge — 5 Hard LeetCode Problems
# ============================================================
# Congratulations on completing 100 Days of Python! 🎉
# Today: solve 5 challenging algorithmic problems.
# ============================================================

# ====================================================================
# Problem 1: Two Sum (LeetCode #1 — Easy warmup)
# Given: array of ints, a target sum.
# Find: indices of two numbers that add up to target.
# ====================================================================
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

assert two_sum([2,7,11,15], 9) == [0,1]
assert two_sum([3,2,4], 6) == [1,2]
print("✅ Problem 1 (Two Sum) passed!")

# ====================================================================
# Problem 2: Longest Substring Without Repeating Characters (LC #3 — Medium)
# ====================================================================
def length_of_longest_substring(s):
    char_index = {}
    max_len = start = 0
    for end, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = end
        max_len = max(max_len, end - start + 1)
    return max_len

assert length_of_longest_substring("abcabcbb") == 3
assert length_of_longest_substring("bbbbb") == 1
assert length_of_longest_substring("pwwkew") == 3
print("✅ Problem 2 (Longest Substring) passed!")

# ====================================================================
# Problem 3: Valid Parentheses (LC #20 — Easy)
# ====================================================================
def is_valid_parentheses(s):
    stack   = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else "#"
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    return not stack

assert is_valid_parentheses("()[]{}") == True
assert is_valid_parentheses("(]") == False
assert is_valid_parentheses("{[]}") == True
print("✅ Problem 3 (Valid Parentheses) passed!")

# ====================================================================
# Problem 4: Climbing Stairs (LC #70 — Easy, DP)
# Each time you can climb 1 or 2 steps. How many ways to climb n steps?
# ====================================================================
def climb_stairs(n):
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

assert climb_stairs(2) == 2
assert climb_stairs(3) == 3
assert climb_stairs(5) == 8
print("✅ Problem 4 (Climbing Stairs) passed!")

# ====================================================================
# Problem 5: Maximum Subarray (LC #53 — Kadane's Algorithm, Medium)
# Find the contiguous subarray with the largest sum.
# ====================================================================
def max_subarray(nums):
    max_sum = current = nums[0]
    for num in nums[1:]:
        current = max(num, current + num)
        max_sum = max(max_sum, current)
    return max_sum

assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert max_subarray([1]) == 1
assert max_subarray([5, 4, -1, 7, 8]) == 23
print("✅ Problem 5 (Maximum Subarray) passed!")

# ====================================================================
print("\n" + "=" * 60)
print("  🎉 ALL 5 PROBLEMS SOLVED! 🎉")
print("=" * 60)
print("""
  ██████╗  ██████╗  ██████╗     ██████╗  █████╗ ██╗   ██╗███████╗
  ╚════██╗██╔═████╗██╔═████╗    ██╔══██╗██╔══██╗╚██╗ ██╔╝██╔════╝
   █████╔╝██║██╔██║██║██╔██║    ██║  ██║███████║ ╚████╔╝ ███████╗
  ██╔═══╝ ████╔╝██║████╔╝██║    ██║  ██║██╔══██║  ╚██╔╝  ╚════██║
  ███████╗╚██████╔╝╚█████╔╝     ██████╔╝██║  ██║   ██║   ███████║
  ╚══════╝ ╚═════╝  ╚════╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝

  🐍 100 Days of Python — COMPLETED! 🐍

  You have mastered:
  ✅ Phase 1: Python Fundamentals (Days 1-25)
  ✅ Phase 2: Data Structures & Tools (Days 26-50)
  ✅ Phase 3: Advanced OOP & Modules (Days 51-75)
  ✅ Phase 4: Web, AI & Career (Days 76-100)

  Next steps:
  🔷 Build your portfolio on GitHub
  🔷 Apply for Python internships/jobs
  🔷 Learn Django, FastAPI, or Data Science (NumPy, Pandas)
  🔷 Keep solving problems on LeetCode daily
  🔷 Contribute to open-source projects

  Keep coding. Keep growing. The journey never ends! 🚀
""")
