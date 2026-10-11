str=input("enter your str: ")
result =""
for ch in str:
    if ch.lower() not in "aeiou":
        result+=ch
print(result)        