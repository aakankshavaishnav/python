# 6. Number-String Conversion Challenge

for i in range(5):
    number = int(input("Enter your number: "))

    number = str(number)

    even = 0
    odd = 0

    for digit in number:
        if int(digit) % 2 == 0:
            even += 1
        else:
            odd += 1

    if even > odd:
        print("Even occurs more")
    elif odd > even:
        print("Odd occurs more")
    else:
        print("Equal")