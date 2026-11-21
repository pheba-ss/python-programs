# set exercises

# Qn1
"""Write a Python program to create a set, add a new element to it, remove an element using remove(), and discard an element using discard().

Given Input: fruits = {"apple", "banana", "cherry"}

Expected Output:

{'apple', 'banana', 'cherry', 'mango'} 
after add, {'apple', 'cherry', 'mango'} 
after remove, {'apple', 'cherry', 'mango'} 
after discard (no error even if element is absent)"""

# Ans
"""fruits = {"apple", "banana", "cherry"}

fruits.add("mango")
print("After add:", fruits)

fruits.remove("banana")
print("After remove:", fruits)

fruits.discard("orange")
print("After discard:", fruits)"""

# Qn2
"""Write a Python program to remove all elements from a set using .clear(), while keeping the variable itself intact.

Given Input: colors = {"red", "green", "blue"}

Expected Output: set()"""

# Ans
"""colors = {"red", "green", "blue"}
colors.clear()
print(colors)"""

# Qn3
"""Write a Python program to determine how many elements are in a set without using the built-in len() function.

Given Input: animals = {"cat", "dog", "bird", "fish"}

Expected Output: Length of set: 4"""

# Ans
"""animals = {"cat", "dog", "bird", "fish"}

count = 0

for item in animals:
    count += 1

print("Length of set:", count)"""

# Qn4
"""Write a Python program to check whether a set is empty using conditional logic, and print an appropriate message based on the result.

Given Input: data = set()

Expected Output: The set is empty."""

# Ans
"""data = set()

if not data:
    print("The set is empty.")
else:
    print("The set is not empty.")"""

# Qn5
"""Write a Python program to combine two sets into one, containing all unique elements from both sets.

Given Input: set_a = {1, 2, 3, 4} and set_b = {3, 4, 5, 6}

Expected Output: Union: {1, 2, 3, 4, 5, 6}"""

# Ans
"""set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

result = set_a.union(set_b)
print("Union:", result)"""

# Qn6
"""Write a Python program to find all elements that are common to both sets.

Given Input: set_a = {1, 2, 3, 4} and set_b = {3, 4, 5, 6}

Expected Output: Intersection: {3, 4}"""

# Ans
"""set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

result = set_a.intersection(set_b)
print("Intersection:", result)"""

# Qn7
"""Write a Python program to find all elements that are present in Set A but not in Set B.

Given Input: set_a = {1, 2, 3, 4} and set_b = {3, 4, 5, 6}

Expected Output: Difference (A - B): {1, 2}"""

# Ans
"""set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

result = set_a.difference(set_b)
print("Difference (A - B):", result)"""

# Qn8
"""Write a Python program to find all elements that are in either Set A or Set B, but not in both.

Given Input: set_a = {1, 2, 3, 4} and set_b = {3, 4, 5, 6}

Expected Output: Symmetric Difference: {1, 2, 5, 6}"""

# Ans
"""set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

result = set_a.symmetric_difference(set_b)
print("Symmetric Difference:", result)"""

# Qn9
"""Write a Python program to identify the largest and smallest values in a set of numbers.

Given Input: numbers = {42, 7, 19, 85, 3, 56}

Expected Output: Max: 85 and Min: 3"""

# Ans
"""numbers = {42, 7, 19, 85, 3, 56}

highest = max(numbers)
lowest = min(numbers)

print("Max:", highest)
print("Min:", lowest)"""

# Qn10
"""Write a Python program to calculate the total sum of all elements in a set manually using a loop, without using the built-in sum() function.

Given Input: numbers = {10, 20, 30, 40, 50}

Expected Output: Sum: 150"""

# Ans
"""numbers = {10, 20, 30, 40, 50}

total = 0

for num in numbers:
    total += num

print("Sum:", total)"""

# Qn11
"""Write a Python program to add multiple elements from a list into an existing set using the .update() method.

Given Input: fruits = {"apple", "banana"} and new_fruits = ["cherry", "mango", "apple"]

Expected Output: Updated set: {'apple', 'banana', 'cherry', 'mango'}"""

# Ans
"""fruits = {"apple", "banana"}
new_fruits = ["cherry", "mango", "apple"]

fruits.update(new_fruits)
print("Updated set:", fruits)"""

# Qn12
"""Write a Python program to add elements from a list, a tuple, and another set into an existing set in a single .update() call.

Given Input: base = {1, 2}, from_list = [3, 4], from_tuple = (5, 6), from_set = {7, 8}

Expected Output: Updated set: {1, 2, 3, 4, 5, 6, 7, 8}"""

# Ans
"""base = {1, 2}

from_list = [3, 4]
from_tuple = (5, 6)
from_set = {7, 8}

base.update(from_list, from_tuple, from_set)
print("Updated set:", base)"""