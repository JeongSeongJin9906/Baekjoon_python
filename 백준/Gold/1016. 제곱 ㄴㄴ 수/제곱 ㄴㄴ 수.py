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
def generate_square_multiples(small,large,prime_number):
    is_square_multiples = [True]*(large-small+1)
    for i in prime_number:
        for j in range(-(small%(i*i)),large-small+1,i*i):
            if j>=0:
                is_square_multiples[j] = False
            else:
                pass
    square_multiples = [i+small for i, square_multiple in enumerate(is_square_multiples) if square_multiple]
    return square_multiples
low,high=tuple(map(int,input().split()))
print(len(generate_square_multiples(low,high,generate_primes(int(math.sqrt(high)+1)))))