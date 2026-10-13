numbers = [12, 5, -4, 18, 0, 25, 30]
for number in numbers:
    if numbers > 0:
        continue
    if numbers ==0:
        break
print("error")    


# ques-2=================================
word = "skyline"

for ch in word:
    if ch in "aeiou":
        break
    print(ch)
    