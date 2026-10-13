
# Q6. Temperature Range

temperature = float(input("Enter temperature: "))

while temperature < -20 or temperature > 45:
    print("Invalid temperature!")
    temperature = float(input("Enter temperature: "))

print("Accepted temperature:", temperature)


# Q7. Withdrawal Validation

balance = 5000

amount = int(input("Enter withdrawal amount: "))

while amount <= 0 or amount > balance:
    print("Invalid withdrawal amount!")
    amount = int(input("Enter withdrawal amount: "))

balance = balance - amount

print("Remaining balance:", balance)


# Q8. Username Validation

username = input("Enter username: ").strip()

while len(username) < 5 or " " in username:
    print("Invalid username!")
    username = input("Enter username: ").strip()

print("Accepted username:", username)


# Q9. Divisible Number

num = int(input("Enter a positive number divisible by 3 and 5: "))

while num <= 0 or num % 3 != 0 or num % 5 != 0:
    print("Invalid number!")
    num = int(input("Enter a positive number divisible by 3 and 5: "))

print("Accepted number:", num)


# Q10. Limited PIN Attempts

secret_pin = 2468
attempts = 0

while attempts < 3:
    pin = int(input("Enter PIN: "))
    attempts = attempts + 1

    if pin == secret_pin:
        print("Access granted!")
        break
    else:
        print("Incorrect PIN!")

if attempts == 3 and pin != secret_pin:
    print("Access denied!")
