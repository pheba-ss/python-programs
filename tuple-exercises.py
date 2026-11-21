# tuple exercises

# Qn1
"""Write a Python program to create a tuple, access its elements by index, and find its length.

Given Input: fruits = ("apple", "banana", "cherry", "date")

Expected Output: First element: apple, Last element: date, and Length: 4"""

# Ans
"""fruits = ("apple", "banana", "cherry", "date")

print("First element:", fruits[0])
print("Last element:", fruits[-1])
print("Length:", len(fruits))"""

# Qn2
"""Write a Python program to create a tuple containing a single item, the number 50, and confirm its type.

Given Input: A single integer value 50

Expected Output: (50,) and <class 'tuple'>"""

# Ans
"""number = (50,)
print(number)
print(type(number))"""

# Qn3
"""Write a Python program to repeat a tuple three times using the * operator.

Given Input: colors = ("red", "green")

Expected Output: ('red', 'green', 'red', 'green', 'red', 'green')"""

# Ans
"""colors = ("red", "green")
result = colors * 3
print(result)"""

# Qn4
"""Write a Python program to join three separate tuples into one new tuple using the + operator.

Given Input: a = (1, 2), b = (3, 4), and c = (5, 6)

Expected Output: (1, 2, 3, 4, 5, 6)"""

# Ans
"""a = (1, 2)
b = (3, 4)
c = (5, 6)

result = a + b + c
print(result)"""

# Qn5
"""Write a Python program to extract a specific portion of a tuple using slice notation.

Given Input: numbers = (10, 20, 30, 40, 50, 60, 70)

Expected Output: (30, 40, 50)"""

# Ans
"""numbers = (10, 20, 30, 40, 50, 60, 70)
result = numbers[2:5]
print(result)"""

# Qn6
"""Write a Python program to reverse the order of elements in a tuple.

Given Input: items = (1, 2, 3, 4, 5)

Expected Output: (5, 4, 3, 2, 1)"""

# Ans
"""items = (1, 2, 3, 4, 5)
result = items[::-1]
print(result)"""

# Qn7
"""Write a Python program to convert a list into a tuple using the tuple() constructor.

Given Input: my_list = [10, 20, 30, 40, 50]

Expected Output: (10, 20, 30, 40, 50) and <class 'tuple'>"""

# Ans
"""my_list = [10, 20, 30, 40, 50]
result = tuple(my_list)
print(result, "and", type(result))"""

# Qn8
"""Write a Python program to convert a tuple of characters into a single joined string.

Given Input: chars = ('a', 'b', 'c')

Expected Output: abc"""

# Ans
"""chars = ('a', 'b', 'c')
result = ''.join(chars)
print(result)"""

# Qn9
"""Write a Python program to check whether a specific element exists inside a tuple using the in keyword.

Given Input: fruits = ("apple", "banana", "cherry", "date")

Expected Output: True and False"""

# Ans
"""fruits = ("apple", "banana", "cherry", "date")
print("banana" in fruits)
print("mango" in fruits)"""

# Qn10
"""Write a Python program to use the .count() method to find how many times a specific element appears in a tuple.

Given Input: votes = ("yes", "no", "yes", "yes", "no", "yes")

Expected Output: yes appears 4 times and no appears 2 times"""

# Ans
"""votes = ("yes", "no", "yes", "yes", "no", "yes")

yes_count = votes.count("yes")
no_count = votes.count("no")

print("yes appears", yes_count, "times")
print("no appears", no_count, "times")"""

# Qn11
"""Write a Python program to unpack a four-element tuple into four distinct variables in a single assignment.

Given Input: person = ("Alice", 30, "Engineer", "Pune")

Expected Output: Name: Alice, Age: 30, Job: Engineer, and City: Pune"""

# Ans
"""person = ("Alice", 30, "Engineer", "Pune")
name, age, job, city = person # unpack the tuple into four variables

print("Name:", name)
print("Age:", age)
print("Job:", job)
print("City:", city)"""

# Qn12
"""Write a Python program to swap the values of two variables using tuple unpacking, without using a temporary third variable.

Given Input: a = 100 and b = 200

Expected Output: After swap: a = 200, b = 100"""

# Ans
"""a = 100
b = 200

a, b = b, a

print("After swap: a =", a, ", " "b =", b)"""

# Qn13
"""Write a Python program to access a specific element that is stored inside a tuple which is itself nested inside another tuple.

Given Input: matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

Expected Output: 6"""

# Ans
"""matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
result = matrix[1][2]
print(result)"""

# Qn14
"""Write a Python program to calculate the total, highest value, and lowest value from a tuple of integers using the built-in sum(), max(), and min() functions.

Given Input: scores = (88, 95, 70, 62, 99, 74, 85)

Expected Output: Sum: 573, Max: 99, and Min: 62"""

# Ans
"""scores = (88, 95, 70, 62, 99, 74, 85)

total = sum(scores)
highest = max(scores)
lowest = min(scores)

print("Sum:", total)
print("Max:", highest)
print("Min:", lowest)"""

# Qn15
"""Write a Python program to sort a tuple of tuples based on the second item in each nested tuple.

Given Input: students = (("Alice", 88), ("Bob", 73), ("Charlie", 95), ("Diana", 61))

Expected Output:

Sorted: (('Diana', 61), ('Bob', 73), ('Alice', 88), ('Charlie', 95))"""

# Ans
"""students = (("Alice", 88), ("Bob", 73), ("Charlie", 95), ("Diana", 61))

result = tuple(sorted(students, key=lambda x: x[1]))
print("Sorted:", result)"""

# Qn16
"""Write a Python program to filter a tuple and keep only the elements that satisfy a given condition, using both filter() and a list comprehension approach.

Given Input: numbers = (3, 14, 7, 22, 9, 41, 18, 5), keep only values greater than 10

Expected Output: Filtered: (14, 22, 41, 18)"""

# Ans
"""numbers = (3, 14, 7, 22, 9, 41, 18, 5)

result1 = tuple(filter(lambda x: x > 10, numbers))
result2 = tuple(x for x in numbers if x > 10)

print("Using filter():", result1)
print("Using list comprehension:", result2)"""

# Qn17
"""Write a Python program to apply a square function to every item in a tuple using map(), and also demonstrate the equivalent generator expression approach.

Given Input: numbers = (1, 2, 3, 4, 5, 6)

Expected Output: Squared: (1, 4, 9, 16, 25, 36)"""

# Ans
"""numbers = (1, 2, 3, 4, 5, 6)

result1 = tuple(map(lambda x: x ** 2, numbers)) # using map() function
result2 = tuple(x ** 2 for x in numbers) # using generator expression

print("Squared using map():", result1)
print("Squared using generator expression:", result2)"""