numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(1, len(numbers)):
    for j in range(1,numbers[i]):
        if numbers[i] / j == 0:
            break
        else:
            primes.append(numbers[i])
print(primes)