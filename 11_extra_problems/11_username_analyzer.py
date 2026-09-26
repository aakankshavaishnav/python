
# 11. Username Analyzer
# Take 5 usernames.

# For every username:

# Check length.
# Check first character.
# Count digits.
# Count underscores.
# Detect invalid special characters.
# Classify each username as:

# "Valid"
# "Needs Improvement"
# "Invalid"
for i in range(5):
    username = input("Enter username: ")

    digits = 0
    underscores = 0
    invalid = False

    for ch in username:
        if ch.isdigit():
            digits += 1
        elif ch == "_":
            underscores += 1
        elif not ch.isalnum():
            invalid = True

    if invalid or not username[0].isalpha():
        print("Invalid")
    elif len(username) < 5:
        print("Needs Improvement")
    else:
        print("Valid")

    print("Length:", len(username))
    print("First character:", username[0])
    print("Digits:", digits)
    print("Underscores:", underscores)



