# n=int(input("enter N: "))
# digit =0
# for i in range (1,n):
#     digit +=1
#     print(i)

n = int(input())
n = abs(n)

if n == 0:
    print(1)
else:
    count = 0
    while n > 0:
        n //= 10
        count += 1
    print(count)