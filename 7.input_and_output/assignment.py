# 11. Convert the string "25" into an integer.

x = "25"
y = int(x)

print(y)


# 12. Convert the string "25.5" into a floating-point number.

p = "25.5"
q = float(p)

print(q)


# 13. Convert the integer 100 into a string.

num = 100
text = str(num)

print(text)


# 14. Take an integer from the user and print its type after conversion.

value = int(input("Enter a number: "))

print(type(value))


# 15. Take a floating-point number from the user and print its type after conversion.

number = float(input("Enter a number: "))

print(type(number))


# 16. Why does this produce string concatenation instead of numeric addition?

first = input()
second = input()

print(first + second)

# input() always returns a string.
# So "10" + "20" gives "1020".


# 17. Correct the program so that it performs numeric addition.

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

print(number1 + number2)


# 18. Create variables name = "Rahul", age = 20
# Use an f-string to display the given sentence.

student_name = "Rahul"
student_age = 20

print(f"My name is {student_name} and I am {student_age} years old.")


# 19. Create a = 10 and b = 20.
# Use an f-string to display their sum.

value1 = 10
value2 = 20

print(f"The sum is {value1 + value2}")


# 20. Take a user's name and age and display them in one sentence using an f-string.

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

print(f"My name is {user_name} and I am {user_age} years old.")


# 21. Take the price of a product as a floating-point value
# and display it using exactly two decimal places.

cost = float(input("Enter price: "))

print(f"Price: {cost:.2f}")


# 22. What is the purpose of :.2f inside an f-string?

# :.2f displays a floating-point number
# with exactly 2 digits after the decimal point.


# 23. Take product name, price and quantity
# and display all three values using f-strings.

item = input("Enter product name: ")
amount = float(input("Enter price: "))
count = int(input("Enter quantity: "))

print(f"Product: {item}")
print(f"Price: {amount:.2f}")
print(f"Quantity: {count}")


# 24. What will this display?

print("A", "B", "C")

# Output:
# A B C


# 25. Rewrite the following so that the values are separated by -.

print("2026", "08", "19", sep="-")


# 26. Write two print() statements that produce Hello World
# on the same line using end.

print("Hello", end=" ")
print("World")


# 27. Take two integers from the user and display:
# First number: <first>
# Second number: <second>
# Sum: <sum>
# Use f-strings.

first_value = int(input("Enter first number: "))
second_value = int(input("Enter second number: "))

total_sum = first_value + second_value

print(f"First number: {first_value}")
print(f"Second number: {second_value}")
print(f"Sum: {total_sum}")


# 28. Take the price and quantity of a product
# and calculate the total cost.
# Display Price, Quantity and Total using an f-string.

product_price = float(input("Enter price: "))
product_quantity = int(input("Enter quantity: "))

final_cost = product_price * product_quantity

print(f"Price: {product_price:.2f}")
print(f"Quantity: {product_quantity}")
print(f"Total: {final_cost:.2f}")


# 29. Take a student's name, age and marks.
# Age should be an integer and marks should be a floating-point value.
# Display all information using a clear formatted message.

learner_name = input("Enter student name: ")
learner_age = int(input("Enter age: "))
score = float(input("Enter marks: "))

print(f"Student Name: {learner_name}")
print(f"Age: {learner_age}")
print(f"Marks: {score:.2f}")


# 30. Create a Student Information program.
# Take name, age, height and city.
# Age should be an integer.
# Height should be a floating-point number.
# Display height with exactly two decimal places.

person_name = input("Enter student name: ")
person_age = int(input("Enter age: "))
person_height = float(input("Enter height: "))
person_city = input("Enter city: ")

print(f"Student Name: {person_name}")
print(f"Age: {person_age}")
print(f"Height: {person_height:.2f}")
print(f"City: {person_city}")