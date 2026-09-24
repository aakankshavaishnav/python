
# # 21
# string = input("Enter a string: ")

# for i in string:
#     print(i)


# # 22
# string = input("Enter a string: ")

# for i in string:
#     print(i, end="")


# 23
string = input("Enter a string: ")

count = 0

for i in string:
    count = count + 1

print(count)


# # 24
# string = input("Enter a string: ")

# count = 0

# for i in string:
#     if i == "a":
#         count = count + 1

# print(count)


# 25
string = input("Enter a string: ")

count = 0

for i in string:
    if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        count = count + 1

print(count)


# # 26
# for i in range(3):
#     for j in range(4):
#         print("*", end="")
#     print()


# # 27
# for i in range(4):
#     for j in range(5):
#         print("*", end="")
#     print()


# # 28
# for i in range(1, 6):
#     for j in range(i):
#         print("*", end="")
#     print()


# # 29
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()


# # 30
# for i in range(1, 6):
#     for j in range(1, 6):
#         print(i * j, end=" ")
#     print()


# # Final Practice Challenge
# n = int(input("Enter n: "))

# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()

