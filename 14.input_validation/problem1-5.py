
# Q1. Valid Marks

marks = int(input("Enter marks: "))

while marks < 0 or marks > 100:
    print("Invalid marks!")
    marks = int(input("Enter marks: "))

print("Accepted marks:", marks)


# Q2. Positive Integer

num = int(input("Enter a positive integer: "))

while num <= 0:
    print("Invalid number!")
    num = int(input("Enter a positive integer: "))

print("Accepted number:", num)


# Q3. Age Validation

age = int(input("Enter age: "))

while age < 0 or age > 120:
    print("Invalid age!")
    age = int(input("Enter age: "))

print("Accepted age:", age)


# Q4. Menu Choice

choice = 0

while choice < 1 or choice > 4:
    print("1. View profile")
    print("2. Edit profile")
    print("3. Settings")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice < 1 or choice > 4:
        print("Invalid choice!")

print("Selected option:", choice)


# Q5. Password Length

password = input("Enter password: ").strip()

while len(password) < 8:
    print("Password must contain at least 8 characters!")
    password = input("Enter password: ").strip()

print("Password accepted!")
