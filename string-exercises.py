# Qn1 - Write a program to create a new string made of an input string’s first, middle, and last characters. Given Input: str1 = "James" Expected Output: Jms
"""str1 = "James"

first = str1[0]
middle = str1[len(str1) // 2]
last = str1[-1]

result = first + middle + last

print(result)"""

# Qn2 -  Write a program to create a new string made of the middle three characters of an input string of odd length. Given Input: str1 = "JhonDipPeta" Expected Output: Dip
"""str1 = "JhonDipPeta"

mid = len(str1) // 2

result = str1[mid - 1:mid + 2]

print(result)"""

# Qn3 - Given two strings, s1 and s2, create a new string by appending s2 in the middle of s1. Given Input: s1 = "Ault" s2 = "Kelly" Expected Output: AuKellylt
"""s1 = "Ault"
s2 = "Kelly"

mid = len(s1) // 2

result = s1[:mid] + s2 + s1[mid:]

print(result)"""

# Qn4 - Given two strings, s1 and s2, create a new string from the first, middle, and last characters of each input string. Given Input: s1 = "America" s2 = "Japan" Expected Output: AJrpan
"""s1 = "America"
s2 = "Japan"

result = s1[0] + s2[0] + s1[len(s1)//2] + s2[len(s2)//2] + s1[-1] + s2[-1]

print(result)"""

# Qn5 - Write a program to reverse a given string. Given Input: str1 = "PYnative" Expected Output: evitanYP
str1 = "PYnative"

result = str1[::-1]

print(result)
