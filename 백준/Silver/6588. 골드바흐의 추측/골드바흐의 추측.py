import math
import sys

# 함수: 소수 생성
def generate_primes(a):
    is_prime = [True] * (a + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(a)) + 1):
        if is_prime[i]:
            for j in range(i * i, a + 1, i):
                is_prime[j] = False
    prime_number = [i for i, prime in enumerate(is_prime) if prime]
    return prime_number

# 함수: 가장 큰 소수 인덱스 찾기
def find_largest_index_less_than(nums, target):
    left, right = 0, len(nums) - 1
    result = 0  # Default value if no element is found
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] <= target:
            result = mid  # Store the current index as potential result
            left = mid + 1  # Search in the right half for larger numbers less than target
        else:
            right = mid - 1  # Search in the left half
    return result

# 빠른 입력 받기
input = sys.stdin.readline
# 빠른 출력 하기
print = sys.stdout.write

# 소수 목록 생성
prime_num = generate_primes(1000000)

# 결과를 저장할 리스트
results = []

while True:
    # 숫자 입력 받기 (단일 숫자 입력 방식)
    a = int(input().strip())  # 한 번에 숫자 입력 받기

    # 입력이 0일 경우 종료
    if a == 0:
        break

    # 계산 수행
    k = find_largest_index_less_than(prime_num, a)
    u = 10

    while True:
        u = 2 * u + 3
        try:
            if k // 2 - u <= 0:
                j = find_largest_index_less_than(prime_num, a // 2)
            else:
                j = k - u
            prime_number_left = set(prime_num[1:u])
            prime_number_right = prime_num[j:k + 1]
            a_difference_prime_number = {a - i for i in prime_number_right}
            total = a_difference_prime_number.intersection(prime_number_left)
            total = list(total)
            m = min(total)
            # 결과를 리스트에 저장
            results.append(f"{a} = {m} + {a - m}\n")
            break
        except:
            continue

# 한 번에 출력 (결과를 모두 합쳐서 출력)
sys.stdout.write("".join(results))