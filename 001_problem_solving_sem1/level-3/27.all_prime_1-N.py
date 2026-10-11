# Q27. All Primes from 1 to N
N = int(input())
for num in range(2, N + 1):
    is_prime = True
    i = 2
    while i * i <= num:
        if num % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print(num, end=" ")