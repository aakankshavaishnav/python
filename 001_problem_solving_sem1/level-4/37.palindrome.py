str=input("enter your str: ")
reverse=""
for ch in str:
    reverse=ch+reverse

if str==reverse:
    print(True)
else:
    print(False)        