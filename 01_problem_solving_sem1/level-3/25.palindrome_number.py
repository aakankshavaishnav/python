# Q25. Palindrome Number
n = int(input())
temp = n
rev = 0
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10
print(rev == n)