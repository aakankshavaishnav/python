n=(input("enter your N: "))
count =0
if ("-" not in n):
    count=len(n)
else:
    count=len(n)-1
print(count)