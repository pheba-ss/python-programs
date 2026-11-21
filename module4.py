# CONTROL STRUCTURES - 26/09/26

#if
"""age=10
if age>=18:
    print("You are eligible to vote")"""
    
#if-else
"""age=15
if age>=18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")"""
   
#elif
"""marks=65

if marks>=90:
    print("Grade A")

elif marks>=75:
    print("Grade B")

elif marks>=50:
    print("Grade C")

else:
    print("Fail")"""
    
#nested-if
"""num=-35

if num>0:
    if num%2==0:
        print("The number is positive and even")

    else:
        print("The number is positive but odd")

else:
    print("The number is not positive")"""
    
#LOOPING STATEMENTS

#for
"""for i in range(5):
    print(i)"""
    
"""for i in range(1,11):
    print(i)"""
    
"""for i in range(2,11,5,):
    print(i)"""
    
#while
"""i=1
while i<=5:
    print(i)
    i+=1"""
    
#break
"""for i in range(1,10):
    print(i)
    if i==5:
        break
else:
    print("Loop finished without break")"""
    
#continue 
"""for i in range(1,10):
    
    if i==5:
        continue
    print(i)"""
    
#pass
"""for i in range(1,10):
    
    if i==5:
        pass
    print(i)"""
  
#Conditional Statements logical programs  
    
#qn1
#Write a program to check whether a number is positive, negative, or zero.
"""num = int(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
else:
    print("The number is negative.")"""

#qn2
#Write a program to check whether a number is even or odd.
"""num = int(input("Enter a number: "))

if num > 0:
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")"""
        
#qn3
#Write a program to check whether a person is eligible to vote based on age.
"""age = int(input("Enter your age: "))
  
if age >= 18: 
    print("Eligible for vote") 
else: 
    print("Not eligible for vote") """
    
#qn4
#Write a program to find the largest of two numbers.
"""first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))

if first_num > second_num:
    print("First number is largest.")
else:
    print("Second number is largest.")"""
    
#qn5
#Write a program to find the smallest of two numbers.
"""first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))

if first_num < second_num:
    print("First number is smaller.")
else:
    print("Second number is smaller.")"""
    
#qn6
#Write a program to find the largest of three numbers.
"""first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
third_num = int(input("Enter the third number: "))

if first_num > second_num and first_num > third_num:
    print("First number is largest.")
elif second_num > first_num and second_num > third_num:
    print("Second number is largest.")
else:
    print("Third number is largest.")"""

#qn7
#Write a program to find the smallest of three numbers.
"""first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
third_num = int(input("Enter the third number: "))

if first_num < second_num and first_num < third_num:
    print("First number is the smallest.")
elif second_num < first_num and second_num < third_num:
    print("Second number is the smallest.")
else:
    print("Third number is the smallest.")"""
    
#qn8
#Write a program to check whether a given year is a leap year.
"""year = int(input("Enter a year: "))

if year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")"""

#qn9
#Write a program to check whether a student has passed or failed based on marks.
"""mark = int(input("Enter your mark: "))

if mark >= 40:
    print("Pass")
else:
    print("Fail")"""
    
#qn10
#Write a program to calculate a student's grade based on marks.
"""mark = int(input("Enter your mark: "))

if mark >= 90:
    print("Grade A")
elif mark >= 70:
    print("Grade B")
elif mark >= 50:
    print("Grade c")
else:
    print("Fail")"""
    
#qn11
#Write a program to check whether a person is eligible for a driving licence based on age.
"""age = int(input("Enter your age: "))
  
if age >= 18: 
    print("Eligible for driving licence") 
else: 
    print("Not eligible for driving licence")"""
    
#qn12
#Write a program to check whether a number is divisible by both 5 and 10.
"""num = int(input("Enter a number: "))

if num % 5 == 0 and num % 10 ==0:
    print("The number is divisible by 5 and 10")
else:
    print("The number is not divisible by 5 and 10")"""
    
#qn13
#Write a program to check whether a number is divisible by 3 or 7.
"""num = int(input("Enter a number: "))

if num % 3 == 0 and num % 7 ==0:
    print("The number is divisible by 5 and 10")
else:
    print("The number is not divisible by 5 and 10")"""
    
#qn14
#Write a program to check whether a given character is a vowel or consonant.
"""character = input("Enter a character: ")

if character == "a" or character == "e"  or character == "i" or character == "o" or character == "u":
    print("Vowel")
else:
    print("Consonant")"""
    
#OR

"""character = input("Enter a character: ")

if character in "AEIOUaeiou":
    print("Vowel")
else:
    print("Consonant")"""
    
#qn15
#Write a program to check whether a number is a two-digit number.
"""num = int(input("Enter a number: "))

if num >= 10 and num <= 99:
    print("two-digit number.")
else:
    print("not a two-digit number.")"""
    
#qn16
#Write a program to check whether a student is eligible for admission if: Marks ≥ 50, Attendance ≥ 75%
"""mark = int(input("Enter your mark: "))
attendance = int(input("Enter your attendance %: "))

if mark >= 50 and attendance >= 75:
    print("student is eligible for admission.")
else:
    print("student is not eligible for admission.")"""
    
#qn17
#Write a program to check whether a person is eligible for a loan if: Age ≥ 21, Salary ≥ ₹25,000
"""age = int(input("Enter your age: "))
salary = int(input("Enter your salary: "))

if age >= 21 and salary >= 25000:
    print("person is eligible for a loan.")
else:
    print("person is not eligible for a loan.")"""
    
#qn18
#Write a program to check whether a number is positive and even.
"""num = int(input("Enter a number: "))

if num > 0 and num % 2 == 0:
    print("number is positive and even.")
else:
    print("number does not satisfy both conditions.")"""
    
#qn19
#Write a program to check whether a number is positive and divisible by 5
"""num = int(input("Enter a number: "))

if num > 0 == 0 and num % 5 == 0:
    print("number is positive and divisible by 5.")
else:
    print("number does not satisfy both conditions.")"""
    
#qn20
#Write a program to check whether a number lies between 10 and 50.
"""num = int(input("Enter a number: "))

if num >= 10 and num <= 50:
    print("number lies between 10 and 50.")
else:
    print("number does not lies between 10 and 50.")"""
    
#qn21
#Write a program to check whether a number is outside the range 10–50.
"""num = int(input("Enter a number: "))

if num < 10 or num > 50:
    print("number is outside the range 10 to 50.")
else:
    print("number is inside the range 10 to 50.")"""
    
#OR

"""num = int(input("Enter a number: "))

if num not in range(10, 51):
    print("number is outside the range 10 to 50.")
else:
    print("number is inside the range 10 to 50.")"""
    
#qn22
#Write a program to accept username and password and display "Login successful" only when both are correct.
"""username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "pheba" and password == "abcd":
    print("Login successful")
else:
    print("Invalid username or password")"""
    
#qn23
#Write a program to check whether a person gets a discount if: Age is above 60 OR Purchase amount is above ₹5000.
"""age = int(input("Enter your age: "))
purchase_amount = input("Enter purchase amount: ")

if age > 60 or purchase_amount > 5000:
    print("eligible for discount")
else:
    print("not eligible for discount")"""
    
#qn24
#Write a program to check whether a student is eligible for an exam using: Attendance ≥ 75 AND Fees paid = True.
"""attendance = int(input("Enter your attendance: "))
fees_paid = True

if attendance >= 75 and fees_paid:
    print("student is eligible for exam.")
else:
    print("student is not eligible for exam.")"""
    
#qn25
#Write a program to check whether a number is divisible by both 3 and 5, only 3, only 5, or neither.
"""num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("Number is divisible by both 3 and 5.")
elif num % 3 == 0:
    print("Number is divisible only by 3.")
elif num % 5 == 0:
    print("Number is divisible only by 5.")
else:
    print("Number is divisible by neither 3 nor 5.")"""
    


# Smart Shopping Cart System

# Get customer details
customer_name = input("Enter Customer Name: ")
product_name = input("Enter Product Name: ")
quantity = int(input("Enter Quantity: "))
price = float(input("Enter Price Per Product: "))
membership = input("Enter Membership Type (Gold, Silver, or Regular): ")
wallet_balance = float(input("Enter Wallet Balance: "))

# Calculate total cost
total_cost = quantity * price

# Calculate discount
if membership == "Gold":
    discount = total_cost * 0.10
elif membership == "Silver":
    discount = total_cost * 0.05
else:
    discount = 0

# Apply discount
total_cost -= discount

# Calculate GST
gst = total_cost * 0.05

# Calculate delivery charge
delivery_charge = 60

if total_cost > 1000 and membership == "Gold":
    delivery_charge = 0

# Calculate final bill
final_bill = total_cost + gst
final_bill += delivery_charge

# Check wallet balance
wallet_sufficient = wallet_balance >= final_bill

# Check product availability
products = ["Rice", "Sugar", "Oil", "Milk", "Bread"]
product_available = product_name in products

# Display customer and product details
print("\n------ CUSTOMER DETAILS ------")
print("Customer Name:", customer_name)
print("Membership Type:", membership)
print("Wallet Balance:", wallet_balance)

print("\n------ PRODUCT DETAILS ------")
print("Product Name:", product_name)
print("Quantity:", quantity)
print("Price Per Product:", price)
print("Product Available:", product_available)

# Display bill details
print("\n------ BILL DETAILS ------")
print("Total Product Cost:", quantity * price)
print("Discount Amount:", discount)
print("Cost After Discount:", total_cost)
print("GST Amount:", gst)
print("Delivery Charge:", delivery_charge)
print("Final Bill Amount:", final_bill)

# Display comparison results
print("\n------ CHECKING CUSTOMER ELIGIBILITY ------")
print("Wallet Balance Sufficient:", wallet_balance >= final_bill)
print("Quantity Greater Than 5:", quantity > 5)
print("Price Less Than 500:", price < 500)
print("GST Less Than or Equal to 100:", gst <= 100)
print("Gold Membership:", membership == "Gold")
print("Not a Regular Member:", membership != "Regular")

# Display logical operator results
free_delivery = final_bill > 1000 and membership == "Gold"
discount_eligible = membership == "Gold" or membership == "Silver"
not_regular = not (membership == "Regular")

print("\n------ CUSTOMER BENEFITS ------")
print("Free Delivery Eligible:", free_delivery)
print("Discount Eligible:", discount_eligible)
print("Customer is Not Regular:", not_regular)

# Demonstrate bitwise operators
a = 5
b = 3

print("\n------ SAMPLE NUMBER OPERATIONS ------")
print("5 & 3 =", a & b)
print("5 | 3 =", a | b)
print("5 ^ 3 =", a ^ b)
print("5 << 1 =", a << 1)
print("5 >> 1 =", a >> 1)

# Demonstrate membership operators
print("\n------ PRODUCT AVAILABILITY ------")
print("Rice Available:", "Rice" in products)
print("Apple Not Available:", "Apple" not in products)

# Demonstrate identity operators
x = 10
y = x
list1 = [1, 2, 3]
list2 = [1, 2, 3]

print("\n------ OBJECT AND VALUE CHECKING ------")
print("x is y:", x is y)
print("x is not y:", x is not y)
print("list1 is list2:", list1 is list2)
print("list1 == list2:", list1 == list2)

# Demonstrate special operators
amount = 100
print("\n------ VALUE AND PRODUCT CHECKING ------")
print("Assigned amount:", amount)
print("Amount equals 100:", amount == 100)
print("x and y refer to the same object:", x is y)
print("Rice exists in products:", "Rice" in products)