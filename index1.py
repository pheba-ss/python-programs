# GETTING STARTED WITH PYTHON - 29/08/2026

# print("Hello World!")

'''print("Hello World!")
print("Hello World!")'''

"""print("Hello World!")
print("Hello World!")"""


"""a=5
b=3
sum=a+b
print("sum is: ",sum)"""


# PYTHON FUNDAMENTALS - 10/09/2026

"""if = 10
print(if)"""

"""name=input("enter: ")
print(name)"""

"""num1=input("Enter 1st number: ")
num2=input("Enter 2nd number: ")
sum=num1+num2
print(sum)"""

"""num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))
sum=num1+num2
print(sum)"""

"""x=10
print(type(x))"""

"""x=3.5
print(isinstance(x, float))
print(isinstance(x, int))"""

"""a=5
b=a
print(id(a))
print(id(b))"""

# OPERATORS & EXPRESSIONS - 19/09/2026

"""a=10
b=4
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)"""

"""x=10
x+=5
print(x)
x-=3
print(x)
x*=2
print(x)"""

#print(5>>2)

#print(5<<2)

#qn1
"""shirt_price = 800
shoes_price = 1200
total_price = shirt_price + shoes_price
print("Shopping bill: ", total_price)"""

#qn2
"""total_balance = 10000
withdraws = 2500
remaining_balance = total_balance-withdraws
print("Bank balance: ", remaining_balance)"""

#qn3
"""One_movie_ticket = 250
total_tickets = 4
total_amount = One_movie_ticket * total_tickets
print("Movie Tickets: ", total_amount)"""

#qn4
"""total_restaurant_bill = 1500
divided_by = 4
sharing_restaurant_bill=total_restaurant_bill/divided_by
print("Sharing a Restaurant Bill: ", sharing_restaurant_bill)"""

#qn5
"""total_chocolates = 53
box_capacity = 10
complete_boxes = total_chocolates // box_capacity
left_chocolates = total_chocolates % box_capacity
print("Complete boxes: ", complete_boxes)
print("Chocolates left: ", left_chocolates)"""

#qn6
"""total_minutes = 145
complete_hours = total_minutes // 60
remaining_minutes = total_minutes % 60
print("Complete hours: ", complete_hours)
print("Remaining minutes: ", remaining_minutes)"""

#qn7
"""roll_number = int(input("Enter student's roll number: "))
if roll_number % 2 == 0:
    print("Roll number is even.")
else:
    print("Roll number is odd.")"""

#qn8
"""square_length = 5
area = 5 ** 2
print("Area of the sqaure: ", area)"""

#qn9
"""digital_wallet = 500
digital_wallet += 200
print("Balance money in the wallet :", digital_wallet)"""

#qn10
"""starting_point = 100
starting_point += 50
starting_point -= 20
print("Final score: ", starting_point)"""

#qn11
"""pass_mark = 40
student_scored = 65
if student_scored >= pass_mark:
    print("Student's mark is greater than or equal to the passing mark.")"""
    
#qn12
"""stored_password = "123"
entered_password = input("enter your password: ")
if entered_password == stored_password:
    print("Password matched.")
else:
    print("Incorrect password.")"""

#qn13
"""stock = input("Checking availability: ")
if stock != 0:
    print("Stock is available.")"""

#qn14
"""age = 20
passed_test = True
if age >= 18 and passed_test == True:
    print("Eligible to apply for driving licence.")
else:
    print("Not eligible to apply for driving licence.")"""
    
#qn15
"""entered_day = input("enter the day: ")
if entered_day == "saturday" or entered_day == "sunday":
    print("It is a weekend.")
else:
    print("It is not a weekend.")"""

#qn16
"""order_amount = 1000
premium_member = True
if order_amount >= 1000 or premium_member == True:
    print("Free delivery is available.")
else:
    print("Delivery charges apply.")"""
    
#qn17
"""account_blocked = False
if not account_blocked:
    print("User can access the account.")
else:
    print("User cannot access the account.")"""
    
#qn18
"""age = 24
graduation_completed = True
banned = False
if age >= 21 and graduation_completed and not banned:
    print("Candidate is eligible for the job.")
else:
    print("Candidate is not eligible for the job.")"""
    
#qn19
"""products = ["Laptop", "Mobile", "Tablet", "Headphones"]
searches = "laptop"
if searches in products:
    print("The product is available.")
else:
    print("The product is not available.")"""
    
#qn20
"""blocked_names = ["admin", "root", "system"]
username = input("Enter the username: ")
if username not in blocked_names:
    print("Username is allowed.")
else:
    print("Username is not allowed.")"""

#qn21
"""email = input("Enter your email: ")
if "@" in email:
    print('"@" in email')
else:
    print('"@" not in email')"""

#qn22
"""list1 = [10, 20, 30]
list2 = [10, 20, 30]
print(list1==list2)
print(list1 is list2)"""

#qn23
"""cart1 = ["Laptop", "Mouse"]
cart2 = cart1
print(cart2)"""

#qn25
"""product_price = 1200
quantity = 3
discount = 500
products = ["Laptop", "Mobile", "Tablet", "Headphones"]
total = product_price * quantity
final_amount = total - discount
if final_amount >= 2000:
    print("Free delivery")
else:
    print("Delivery charges apply")
if "Laptop" in products:
    print("Laptop is available.")
else:
    print("Laptop is not available.")"""
    
    
# Online Food Ordering System

# Variables store the values entered by the user.
customer_name = input("Enter customer name: ")
food_item = input("Enter food item: ")

# Explicit type conversion:
# input() gives a string, so we convert quantity to integer.
quantity = int(input("Enter quantity: "))

# Convert price to float.
price_per_item = float(input("Enter price per item: "))

# Convert delivery distance to float.
delivery_distance = float(input("Enter delivery distance: "))


# Calculate total food cost.
total_food_cost = quantity * price_per_item

# Calculate delivery charge - ₹5 per km
delivery_charge = delivery_distance * 5

# Implicit type conversion:
# total_food_cost is float and delivery_charge is float - Python automatically handles the calculation.
final_bill = total_food_cost + delivery_charge

# Display order details
print("\n------ ORDER DETAILS ------")

print("\nCustomer name:", customer_name)
print("Type:", type(customer_name))
print("Memory address:", id(customer_name))

print("\nFood item:", food_item)
print("Type:", type(food_item))
print("Memory address:", id(food_item))

print("\nQuantity:", quantity)
print("Type:", type(quantity))
print("Memory address:", id(quantity))

print("\nPrice per item:", price_per_item)
print("Type:", type(price_per_item))
print("Memory address:", id(price_per_item))

print("\nDelivery distance:", delivery_distance)
print("Type:", type(delivery_distance))
print("Memory address:", id(delivery_distance))

# Checking data types using isinstance()
print("\nChecking data types:")
print("Quantity is integer:", isinstance(quantity, int))
print("Price is float:", isinstance(price_per_item, float))
print("Final bill is float:", isinstance(final_bill, float))

# Display final bill
print("\nTotal Food Cost:", total_food_cost)
