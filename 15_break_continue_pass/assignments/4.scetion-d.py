for i in range(1,6):
    if i %2==0:
        pass 
    print(i)
#  ==========================   #
#  ques=32
# choice=input("enter your choice: ")
# if choice=="1":
#     print("option 1 selected ")
# elif choice =="2":
#     print("option 2")
#     pass 
# else: 
#     print("unknown option") 
# print("program closed")

# ques-33
for i in range(1, 5):
    if i == 3:
        continue
    print(i)
for i in range(1, 5):
    if i == 3:
        pass
    print(i)
# ques-34

for i in range(1, 5):
    if i == 3:
        pass
    print(i)
# ques-35    # 
for i in range(1, 6):
    if i == 2:
        continue
    if i == 4:
        break
    print(i)
else:
    print("Finished")

# ques=36    # 
numbers = [10, -5, 20, 30, -2]
target = 20

for num in numbers:
    if num < 0:
        continue

    if num == target:
        print("Target found")
        break
else:
    print("Target not found")

# ques=38    
for row in range(1, 4):
    for col in range(1, 4):
        if col == 2:
            continue
        if row == 3:
            break
        print(row, col)
    else:
        print("Inner loop completed")

        # ques=39
        numbers = [-3, 8, 12, 24]

for num in numbers:
    if num < 0:
        continue

    if num % 4 == 0 and num % 6 == 0:
        print("Found:", num)
        break
else:
    print("No matching number")

    