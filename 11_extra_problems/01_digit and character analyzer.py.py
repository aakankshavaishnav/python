
text = input("Enter a string: ")

uppercase = 0
lowercase = 0
digits = 0
spaces = 0
special = 0

for ch in text:
    if ch.isupper():
        uppercase += 1
    elif ch.islower():
        lowercase += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    else:
        special += 1

print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)

highest = max(uppercase, lowercase, digits, spaces, special)

count = 0

if uppercase == highest:
    count += 1
if lowercase == highest:
    count += 1
if digits == highest:
    count += 1
if spaces == highest:
    count += 1
if special == highest:
    count += 1

if count > 1:
    print("Tie")
elif uppercase == highest:
    print("Uppercase has the highest count")
elif lowercase == highest:
    print("Lowercase has the highest count")
elif digits == highest:
    print("Digits have the highest count")
elif spaces == highest:
    print("Spaces have the highest count")
else:
    print("Special characters have the highest count")