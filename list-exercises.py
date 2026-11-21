# Qn1
""" Write a script to perform the following three operations on given list

Access the third element of a list
List Length: Print the total number of items
Check if the list is empty

Given Input: numbers = [10, 20, 30, 40, 50]

Expected Output:

Third element: 30
Length of list: 5
Is the list empty? False """

# Ans
"""numbers = [10, 20, 30, 40, 50]

print("Third element:", numbers[2])
print("Length of list:", len(numbers))
print("Is the list empty?", len(numbers) == 0)"""

# Qn2
"""Take a given list and modify it through five specific actions:

Change Element: Change the second element of a list to 200 and print the updated list.
Append Element: Add 600 o the end of a list and print the new list.
Insert Element: Insert 300 at the third position (index 2) of a list and print the result.
Remove Element (by value): Remove 600 from the list and print the list.
Remove Element (by index): Remove the element at index 0 from the list print the list.


Given Input: Initial List: [100, 50, 400, 500]

Expected Output:

Updated (Change): [100, 200, 400, 500]
Updated (Append): [100, 200, 400, 500, 600]
Updated (Insert): [100, 200, 300, 400, 500, 600]
Updated (Remove 600): [100, 200, 300, 400, 500]
Updated (Remove Index 0): [200, 300, 400, 500] """

# Ans
"""numbers = [100, 50, 400, 500]

numbers[1] = 200
print("Updated (Change):", numbers) #Change Element

numbers.append(600)
print("Updated (Append):", numbers) #Append Element

numbers.insert(2, 300)
print("Updated (Insert):", numbers) #Insert Element

numbers.remove(600)
print("Updated (Remove 600):", numbers) #Remove Element (by value)

numbers.pop(0)
print("Updated (Remove Index 0):", numbers) #Remove Element (by index)"""

# Qn3
"""Calculate the total sum of all integers in a list and find the arithmetic mean (average).

Given Input: Numbers: [10, 20, 30, 40, 50]

Expected Output:

Sum: 150
Average: 30.0"""

# Ans
"""numbers = [10, 20, 30, 40, 50]

total = sum(numbers)
average = total / len(numbers)

print("Sum:", total)
print("Average:", average)"""

# Qn4
"""Find Maximum and Minimum from List
Practice Problem: Identify the largest and smallest numerical values within a provided list.

Given Input: Data: [45, 12, 89, 2, 67]

Expected Output:

Maximum: 89
Minimum: 2"""

# Ans
"""numbers = [45, 12, 89, 2, 67]

maximum = max(numbers)
minimum = min(numbers)

print("Maximum:", maximum)
print("Minimum:", minimum)"""

# Qn5
"""Multiply every number in a list together to find the total product.

Given Input: Factors: [2, 3, 5, 7]

Expected Output: Product: 210"""

# Ans
"""factors = [2, 3, 5, 7]

product = 1

for num in factors:
    product = product * num

print("Product:", product)"""

# Qn6
"""Given a list of integers, iterate through the items and count how many are even and how many are odd.

Given Input: Numbers: [10, 21, 4, 45, 66, 93, 11]

Expected Output:

Even numbers: 3
Odd numbers: 4"""

# Ans
"""numbers = [10, 21, 4, 45, 66, 93, 11]

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)"""

# Qn7
"""Take a list and reverse the order of its elements.

Given Input: List: [100, 200, 300, 400, 500]

Expected Output: Reversed List: [500, 400, 300, 200, 100]"""

# Ans
"""numbers = [100, 200, 300, 400, 500]

numbers.reverse()

print("Reversed List:", numbers)"""

# Qn8
"""Sort a list of numbers in ascending order (lowest to highest).

Given Input: Unsorted: [56, 12, 89, 3, 22]

Expected Output: Sorted List: [3, 12, 22, 56, 89]"""

# Ans
"""numbers = [56, 12, 89, 3, 22]

numbers.sort()
print("Sorted List:", numbers)"""

# Qn9
"""Create a copy of an existing list so that modifying the copy does not change the original.

Given Input: Original: ["Apple", "Banana", "Cherry"]

Expected Output:

Original: ['Apple', 'Banana', 'Cherry']
Copy: ['Apple', 'Banana', 'Cherry']
(Verification: Modifying copy doesn't hurt original!)"""

# Ans
original = ["Apple", "Banana", "Cherry"]

copy_list = original.copy()

copy_list[0] = "Mango"

print("Original:", original)
print("Copy:", copy_list)

# Qn10
"""Merge two separate lists into a single, unified list.

Given Input:

List A: ["Physics", "Chemistry"]
List B: ["Maths", "Biology"]
Expected Output: Combined List: ['Physics', 'Chemistry', 'Maths', 'Biology']"""

# Ans
"""list_a = ["Physics", "Chemistry"]
list_b = ["Maths", "Biology"]

combined_list = list_a + list_b

print("Combined List:", combined_list)"""