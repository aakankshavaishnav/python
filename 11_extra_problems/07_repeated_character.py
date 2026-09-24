# Take a string.

# For every character, determine how many times it appears in the string without using count().

# Print only characters that appear more than once.

# Also classify them:

# 2 occurrences → "Duplicate"
# 3–4 occurrences → "Repeated"
# More than 4 → "Highly Repeated"
# text=input("enter your string: ")
# for ch in text:
#     frequency =0
#     for x in text:
#         if ch==x:
#             frequency +=1
#     if frequency >1:
#         if frequency==2:
#             print(ch,"duplicated")   
#     elif frequency>=4:
#         print(ch,"repeated")
#     else:
#         print(ch,"highlyrepeated")
text = input("Enter a string: ")

for ch in text:
    frequency = 0

    for x in text:
        if ch == x:
            frequency += 1

    if frequency > 1:
        if frequency == 2:
            print(ch, "Duplicate")
        elif frequency <= 4:
            print(ch, "Repeated")
        else:
            print(ch, "Highly Repeated")

