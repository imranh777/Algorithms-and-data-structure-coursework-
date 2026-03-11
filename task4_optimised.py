import math
import time

# cache to store previous prime results
prime_cache = {}


def is_prime(n):

    if n in prime_cache:
        return prime_cache[n]

    if n < 2:
        prime_cache[n] = False
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            prime_cache[n] = False
            return False

    prime_cache[n] = True
    return True


def prime_dense_window(number_string, W, N):

    if not number_string.isdigit():
        return "0, 0: Invalid input"

    best_index = 0
    max_count = 0
    best_primes = set()

    for i in range(len(number_string) - W + 1):

        window = number_string[i:i+W]
        primes_found = set()

        for start in range(len(window)):
            for end in range(start + 1, len(window) + 1):

                substring = window[start:end]
                number = int(substring)

                if number < N and is_prime(number):
                    primes_found.add(number)

        if len(primes_found) > max_count:
            max_count = len(primes_found)
            best_index = i
            best_primes = primes_found

    if max_count == 0:
        return "0, 0: No primes found"

    primes_list = sorted(best_primes)

    return f"{best_index}, {max_count}: {', '.join(map(str, primes_list))}"


# runtime measurement
start_time = time.time()

print(prime_dense_window("3141592653", 3, 50))

end_time = time.time()

print("Runtime:", end_time - start_time, "seconds")