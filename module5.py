# FUNCTIONS IN PYTHON - 03/10/2026

"""def find_square(x):
    print(x*x)
print(find_square(5))"""

"""def test():
    print("A")
    return
    print("B")
test()"""

"""def stats(a, b):
    return a + b, a * b
s, p = stats(2, 4)
print("Sum:", s)
print("Product:", p)"""


# Loop-Based Logical Programs

# Qn1 - Write a program to print numbers from 1 to 100.
"""for i in range(1, 101):
    print(i)"""
    
# Qn2 - Write a program to print numbers from 100 to 1.
"""for i in range(100, 0):
    print(i)"""
    
# Qn3 - Write a program to print all even numbers from 1 to 100.
"""for i in range(2, 101, 2): 
    print(i)"""
    
# Qn4 - Write a program to print all odd numbers from 1 to 100.
"""for i in range(1, 100, 2): 
    print(i)"""
    
# Qn5 - Write a program to print all numbers between 1 and 100 that are divisible by 5.
"""for i in range(5, 101, 5):
    print(i)"""
    
# Qn6 - Write a program to calculate the sum of numbers from 1 to 100.
"""total = 0

for i in range(1, 101):
    total += i

print("Sum =", total)"""

# Qn7 - Write a program to calculate the sum of even numbers from 1 to 100.
"""total = 0

for i in range(2, 101, 2):
    total += i

print("Sum of even numbers =", total)"""

# Qn8 - Write a program to calculate the sum of odd numbers from 1 to 100.
"""total = 0

for i in range(1, 101, 2):
    total += i

print("Sum of odd numbers =", total)"""

# Qn9 - Write a program to calculate the product of numbers from 1 to 10.
"""product = 1

for i in range(1, 11):
    product *= i

print("Product =", product)"""

# Qn10 - Write a program to print the multiplication table of a given number.
"""num = int(input("Enter a number: "))

for i in range(1, 11):
    print(i, "x", num, "=", num * i)"""
    
# Qn11 - Write a program to print multiplication tables from 1 to 5.
"""for num in range(1, 6):
    print("Table of", num)

    for i in range(1, 11):
        print(i, "x", num, "=", num * i)

    print()"""
    
# Qn12 - Write a program to count how many numbers between 1 and 100 are divisible by 3.
"""count = 0

for i in range(1, 101):
    if i % 3 == 0:
        count += 1

print("Count =", count)"""

# Qn13 - Write a program to print numbers from 1 to 50 but skip multiples of 5.
"""for i in range(1, 51):
    if i % 5 == 0:
        continue
    print(i)"""
    
# Qn14 - Write a program to print numbers from 1 to 100 and stop when the first multiple of 17 is found.
"""for i in range(1, 101):
    print(i)

    if i % 17 == 0:
        break"""
        
# Qn15 - Write a program to print numbers from 1 to 20, but skip even numbers using continue.
"""for i in range(1, 21):
    if i % 2 == 0:
        continue
    print(i)"""

# Number Logic

# Qn16 - Write a program to find the factorial of a number.
"""num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial =", factorial)"""

# Qn17 - Write a program to find the sum of digits of a number. Example: Input: 1234, Output: 10
"""num = int(input("Enter a number: "))
total = 0

while num > 0:
    digit = num % 10
    total += digit
    num //= 10

print("Sum of digits =", total)"""

# Qn18 - Write a program to count the number of digits in a number.
"""num = int(input("Enter a number: "))
count = 0

while num > 0:
    count += 1
    num //= 10

print("Number of digits =", count)"""

# Qn19 - Write a program to reverse a number. Example: Input: 1234, Output: 4321
"""num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reversed number =", reverse)"""

# Qn20 - Write a program to check whether a number is a palindrome. Example: 121 → Palindrome, 123 → Not Palindrome
"""num = int(input("Enter a number: "))
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")"""
    
# Qn21 - Write a program to check whether a number is an Armstrong number.
"""num = int(input("Enter a number: "))
original = num
digits = len(str(num))
total = 0

while num > 0:
    digit = num % 10
    total = total + digit ** digits
    num = num // 10

if original == total:
    print("Armstrong number")
else:
    print("Not an Armstrong number")"""

# Qn22 - Write a program to check whether a number is a prime number.
"""num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
else:
    print("Not a prime number")"""
    
# Qn23 - Write a program to print all prime numbers between 1 and 100.
"""for num in range(2, 101):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)"""
        
# Qn24 - Write a program to count the number of factors of a given number.
"""num = int(input("Enter a number: "))
count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count += 1

print("Number of factors =", count)"""

# Qn25 - Write a program to find the sum of all factors of a number.
"""num = int(input("Enter a number: "))
total = 0

for i in range(1, num + 1):
    if num % i == 0:
        total += i

print("Sum of factors =", total)"""

# Qn26 - Write a program to find the largest digit in a number. Example: Input: 5832, Output: 8
"""num = int(input("Enter a number: "))
largest = 0

while num > 0:
    digit = num % 10

    if digit > largest:
        largest = digit

    num //= 10

print("Largest digit =", largest)"""

# Qn27 - Write a program to find the smallest digit in a number.
"""num = int(input("Enter a number: "))
smallest = 9

while num > 0:
    digit = num % 10

    if digit < smallest:
        smallest = digit

    num //= 10

print("Smallest digit =", smallest)"""

# Qn28 - Write a program to count how many even digits are present in a number.
"""num = int(input("Enter a number: "))
count = 0

while num > 0:
    digit = num % 10

    if digit % 2 == 0:
        count += 1

    num //= 10

print("Count of even digits =", count)"""

# Qn29 - Write a program to count how many odd digits are present in a number.
"""num = int(input("Enter a number: "))
count = 0

while num > 0:
    digit = num % 10

    if digit % 2 != 0:
        count += 1

    num //= 10

print("Count of odd digits =", count)"""

# Qn30 - Write a program to find the sum of even digits in a number.
"""num = int(input("Enter a number: "))
total = 0

while num > 0:
    digit = num % 10

    if digit % 2 == 0:
        total += digit

    num //= 10

print("Sum of even digits =", total)"""

# Qn31 - Write a program to find the sum of odd digits in a number.
"""num = int(input("Enter a number: "))
total = 0

while num > 0:
    digit = num % 10

    if digit % 2 != 0:
        total += digit

    num //= 10

print("Sum of odd digits =", total)"""

# Qn32 - Write a program to check whether a number contains the digit 5.
"""num = int(input("Enter a number: "))

while num > 0:
    digit = num % 10

    if digit == 5:
        print("The number contains digit 5")
        break

    num //= 10
else:
    print("The number does not contain digit 5")"""
    
# Qn33 - Write a program to find how many times the digit 7 occurs in a number.
"""num = int(input("Enter a number: "))
count = 0

while num > 0:
    digit = num % 10

    if digit == 7:
        count += 1

    num //= 10

print("Digit 7 occurs", count, "times")"""

# Qn34 - Write a program to print all the factors of a number.
"""num = int(input("Enter a number: "))

for i in range(1, num + 1):
    if num % i == 0:
        print(i)"""
        
# Qn35 - Write a program to determine whether a number is a perfect number.
"""num = int(input("Enter a number: "))
total = 0

for i in range(1, num):
    if num % i == 0:
        total += i

if total == num and num > 0:
    print("Perfect number")
else:
    print("Not a perfect number")"""
    
    
# break, continue, pass Logic

# Qn1 - Write a program to search for a given number in a range from 1 to 100. Stop the loop when the number is found using break.
"""num = int(input("Enter a number to search (1 to 100): "))

for i in range(1, 101):
    if i == num:
        print("Number found:", i)
        break"""
        
# Qn2 - Write a program to print numbers from 1 to 50 but skip numbers divisible by 3 using continue.
"""for i in range(1, 51):
    if i % 3 == 0:
        continue
    print(i)"""
    
# Qn3- Write a program to print numbers from 1 to 100 and stop at the first number divisible by both 7 and 11.
"""for i in range(1, 101):
    print(i)

    if i % 7 == 0 and i % 11 == 0:
        break"""
        
# Qn4 - Write a program to print only odd numbers from 1 to 50 using continue.
"""for i in range(1, 51):
    if i % 2 == 0:
        continue
    print(i)"""
    
# Qn5 - Write a program that repeatedly accepts numbers and stops when the user enters 0, using break.
"""while True:
    num = int(input("Enter a number: "))

    if num == 0:
        print("Loop stopped")
        break

    print("You entered:", num)"""
    
# Qn6 - Write a program that accepts numbers repeatedly and skips negative numbers using continue.
"""while True:
    num = int(input("Enter a number: "))

    if num < 0:
        continue

    print("You entered:", num)"""
    
# Qn7 - Write a program to print numbers from 1 to 20 but do nothing when the number is 10 using pass.
"""for i in range(1, 21):
    if i == 10:
        pass
    print(i)"""
    
# Qn8 - Write a program to search for the first even number in a given sequence and stop using break.
"""numbers = [3, 7, 9, 12, 15, 18]

for num in numbers:
    if num % 2 == 0:
        print("First even number:", num)
        break"""

# Qn9 - Write a program to print all numbers between 1 and 100 except multiples of both 3 and 5.
"""for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        continue
    print(i)"""
    
# Qn10 - Write a program that keeps accepting marks until the user enters -1, then displays the total number of students entered. break, continue, pass Logic
"""count = 0

while True:
    marks = int(input("Enter student marks (-1 to stop): "))

    if marks == -1:
        break

    if marks < 0:
        continue

    pass
    count += 1

print("Total number of students:", count)"""

# Higher logic questions

# Qn11 - Write a program to find the second-largest number among three numbers.
"""a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if (a >= b and a <= c) or (a <= b and a >= c):
    print("Second-largest number =", a)
elif (b >= a and b <= c) or (b <= a and b >= c):
    print("Second-largest number =", b)
else:
    print("Second-largest number =", c)"""
    
# Qn12 - Write a program to find the second-smallest number among three numbers.
"""a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if (a >= b and a <= c) or (a <= b and a >= c):
    print("Second-smallest number =", a)
elif (b >= a and b <= c) or (b <= a and b >= c):
    print("Second-smallest number =", b)
else:
    print("Second-smallest number =", c)"""
    
# Qn13 - Write a program to find the GCD/HCF of two numbers using a loop.
"""a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

gcd = 1

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

print("GCD/HCF =", gcd)"""

# Qn14 - Write a program to find the LCM of two numbers using a loop.
"""a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

lcm = max(a, b)

while True:
    if lcm % a == 0 and lcm % b == 0:
        break
    lcm += 1

print("LCM =", lcm)"""
    
# Qn15 - Write a program to generate the Fibonacci series up to n terms.
"""n = int(input("Enter the number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c"""
    
# Qn16 - Write a program to check whether two numbers are co-prime.
"""a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

gcd = 1

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

if gcd == 1:
    print("Co-prime numbers")
else:
    print("Not co-prime numbers")"""
    
# Qn17 - Write a program to find the largest and smallest digit of a number in a single program.
"""num = int(input("Enter a number: "))

largest = 0
smallest = 9

while num > 0:
    digit = num % 10

    if digit > largest:
        largest = digit

    if digit < smallest:
        smallest = digit

    num //= 10

print("Largest digit =", largest)
print("Smallest digit =", smallest)"""

# Qn18 - Write a program to check whether a number is both palindrome and prime.
"""num = int(input("Enter a number: "))

# Check palindrome
temp = num
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if num == reverse:
    palindrome = True
else:
    palindrome = False

# Check prime
count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count += 1

if count == 2:
    prime = True
else:
    prime = False

# Check both conditions
if palindrome and prime:
    print("The number is both palindrome and prime")
else:
    print("The number is not both palindrome and prime")"""
    
# Qn19 - Write a program to print all Armstrong numbers between 1 and 1000.
"""for num in range(1, 1001):
    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10
        total = total + digit ** 3
        temp //= 10

    if total == num:
        print(num)"""
        
# Qn20 - Write a program to print all perfect numbers between 1 and 1000.
"""for num in range(1, 1001):
    total = 0

    for i in range(1, num):
        if num % i == 0:
            total = total + i

    if total == num:
        print(num)"""