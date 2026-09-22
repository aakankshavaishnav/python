for i in range(1, 6):
    password = input("Enter password: ")
    count = 0
    if len(password) >= 8:
        count += 1
    for ch in password:
        if ch.isupper():
            count += 1
            break
    for ch in password:
        if ch.islower():
            count += 1
            break
    for ch in password:
        if ch.isdigit():
            count += 1
            break
    for ch in password:
        if not ch.isalnum():
            count += 1
            break
    if count == 5:
        print("Strong")
    elif count >= 3:
        print("Medium")
    else:
        print("Weak")