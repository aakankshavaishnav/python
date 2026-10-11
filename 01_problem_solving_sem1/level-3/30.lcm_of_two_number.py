# Q30. LCM of Two Numbers
a = int(input())
b = int(input())
m = max(a, b)
while m % a != 0 or m % b != 0:
    m += 1
print(m)