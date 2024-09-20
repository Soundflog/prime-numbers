# Функции проверки одного числа на простоту
from limit_primes_number import is_prime_basic, miller_rabin


def is_prime_basic_single(n):
    """Проверка, является ли число простым (метод простой проверки делением)."""
    return is_prime_basic(n)


def sieve_of_eratosthenes_single(n):
    """Проверка, является ли число простым (метод Решета Эратосфена)."""
    if n < 2:
        return False
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return sieve[n]


def sieve_of_atkin_single(n):
    """Проверка, является ли число простым (метод Решета Аткина)."""
    if n < 2:
        return False
    sieve = [False] * (n + 1)
    sieve[2] = sieve[3] = True

    for x in range(1, int(n ** 0.5) + 1):
        for y in range(1, int(n ** 0.5) + 1):
            num = 4 * x ** 2 + y ** 2
            if num <= n and (num % 12 == 1 or num % 12 == 5):
                sieve[num] = not sieve[num]
            num = 3 * x ** 2 + y ** 2
            if num <= n and num % 12 == 7:
                sieve[num] = not sieve[num]
            num = 3 * x ** 2 - y ** 2
            if x > y and num <= n and num % 12 == 11:
                sieve[num] = not sieve[num]

    for i in range(5, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i * i):
                sieve[j] = False
    return sieve[n]


def miller_rabin_single(n, k=5):
    """Проверка, является ли число простым (метод теста Миллера-Рабина)."""
    return miller_rabin(n, k)
