# ques-=1 
for i in range(1, 4):
    print(i)
else:
    print("Done")

#qus=2 =========
for i in range(1, 5):
    if i == 2:
        continue
    print(i)
else:
    print("Completed")

# ques-22 =============
#  Take a list of integers and a target number. If the target exists, print "Found". Otherwise, print "Not found" using for-else.
# Test cases
# List Target Expected output
n=int(input("enter your n: "))
for i in range(10):
    if n ==3:
        print("found")
        break

else:
    print("not found")

# ques=23 Take a string and a target character. Use for-else to print "Character exists" if found, or "Character missing" otherwise.
# Test cases
# String Target Expected output
text = input("Enter a string: ")
target = input("Enter target character: ")

for ch in text:
    if ch == target:
        print("Character exists")
        break
else:
    print("Character missing")

    # ques=24
    # ====================================
    def prime(n):

    count = 0
    factor = 1

    while factor <= n:
        if n % factor == 0:
            count += 1
        factor += 1

    if count == 2:
        print("prime")
    else:
        print("not a prime")

# ===========================        
# ques=27
