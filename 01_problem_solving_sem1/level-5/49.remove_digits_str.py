str=input("enter your str: ")
result=""
for ch in str:
    if not (ch>="0" and ch <="9"):
        result +=ch
print(result)        