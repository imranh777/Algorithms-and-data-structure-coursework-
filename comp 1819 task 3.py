import math
import time

def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True

def prime_dense_window_dict(s, W, N):

    if not s.isdigit() or W > len(s):
        return "0, 0: Invalid input"

    length = len(s)

    best_index = 0
    max_primes = 0
    best_prime_list = []

    for start in range(length - W + 1):

        window = s[start:start + W]

        primes_found = {}

        for i in range(W):
            for j in range(i + 1, W + 1):

                substring = window[i:j]
                number = int(substring)

                if number < N and is_prime(number):

                    if number not in primes_found:
                        primes_found[number] = 1
                    else:
                        primes_found[number] += 1

        unique_primes = sorted(primes_found.keys())

        if len(unique_primes) > max_primes:
            max_primes = len(unique_primes)
            best_index = start
            best_prime_list = unique_primes

    if max_primes == 0:
        return "0, 0: No primes found"

    if len(best_prime_list) >= 6:
        display = best_prime_list[:3] + best_prime_list[-3:]
    else:
        display = best_prime_list

    return f"{best_index}, {max_primes}: {display}"


# -----------------------
# Runtime measurement
# -----------------------

start_time = time.time()

# Example test case
print(prime_dense_window_dict("3141592653", 2, 100))

end_time = time.time()

print("Runtime:", end_time - start_time, "seconds")

