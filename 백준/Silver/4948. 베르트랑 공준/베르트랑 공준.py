import math
def generate_primes(a):
    is_prime = [True] * (a + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(a)) + 1):
        if is_prime[i]:
            for j in range(i * i, a + 1, i):
                is_prime[j] = False
    prime_number = [i for i, prime in enumerate(is_prime) if prime]
    return prime_number
while True:
    a=int(input())
    if a==0:
        break
    print(len(generate_primes(2*a))-len(generate_primes(a)))