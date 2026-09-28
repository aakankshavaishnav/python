# #question11
# 11. Convert the string "25" into an integer.

a = "25"
b = int(a)

print(b)


# 12. Convert the string "25.5" into a floating-point number.

a = "25.5"
b = float(a)

print(b)


# 13. Convert the integer 100 into a string.

a = 100
b = str(a)

print(b)


# 14. Take an integer from the user and print its type after conversion.

a = int(input("Enter a number: "))

print(type(a))


# 15. Take a floating-point number from the user and print its type after conversion.

a = float(input("Enter a number: "))

print(type(a))


# 16. Why does this produce string concatenation instead of numeric addition?

a = input()
b = input()

print(a + b)

# input() always returns a string.
# Therefore, "10" + "20" gives "1020".


# 17. Correct the program so that it performs numeric addition.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a + b)


# 18. Create variables name = "Rahul", age = 20
# Use an f-string to display the given sentence.

name = "Rahul"
age = 20

print(f"My name is {name} and I am {age} years old.")


# 19. Create a = 10 and b = 20.
# Use an f-string to display their sum.

a = 10
b = 20

print(f"The sum is {a + b}")


# 20. Take a user's name and age and display them in one sentence using an f-string.

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"My name is {name} and I am {age} years old.")


# 21. Take the price of a product as a floating-point value
# and display it using exactly two decimal places.

price = float(input("Enter price: "))

print(f"Price: {price:.2f}")


# 22. What is the purpose of :.2f inside an f-string?

# :.2f displays a floating-point number
# with exactly 2 digits after the decimal point.


# 23. Take product name, price and quantity
# and display all three values using f-strings.

product = input("Enter product name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

print(f"Product: {product}")
print(f"Price: {price:.2f}")
print(f"Quantity: {quantity}")


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

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

sum = first + second

print(f"First number: {first}")
print(f"Second number: {second}")
print(f"Sum: {sum}")


# 28. Take the price and quantity of a product
# and calculate the total cost.
# Display Price, Quantity and Total using an f-string.

price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print(f"Price: {price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total: {total:.2f}")


# 29. Take a student's name, age and marks.
# Age should be an integer and marks should be a floating-point value.
# Display all information using a clear formatted message.

name = input("Enter student name: ")
age = int(input("Enter age: "))
marks = float(input("Enter marks: "))

print(f"Student Name: {name}")
print(f"Age: {age}")
print(f"Marks: {marks:.2f}")


# 30. Create a Student Information program.
# Take name, age, height and city.
# Age should be an integer.
# Height should be a floating-point number.
# Display height with exactly two decimal places.

name = input("Enter student name: ")
age = int(input("Enter age: "))
height = float(input("Enter height: "))
city = input("Enter city: ")

print(f"Student Name: {name}")
print(f"Age: {age}")
print(f"Height: {height:.2f}")
print(f"City: {city}")