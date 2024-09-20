def is_prime_basic(n):
    """Проверка делением: является ли число простым."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def primes_basic(limit):
    """Нахождение всех простых чисел до limit методом простой проверки делением."""
    primes = []
    for num in range(2, limit + 1):
        if is_prime_basic(num):
            primes.append(num)
    return primes


# Алгоритм Решето Эратосфена
def sieve_of_eratosthenes(limit):
    """Нахождение всех простых чисел до limit с помощью Решета Эратосфена."""
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0 и 1 не являются простыми
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return [x for x in range(limit + 1) if sieve[x]]


# Алгоритм Решето Аткина
def sieve_of_atkin(limit):
    """Нахождение всех простых чисел до limit с помощью Решета Аткина."""
    sieve = [False] * (limit + 1)
    sieve[2] = sieve[3] = True  # 2 и 3 являются простыми

    for x in range(1, int(limit ** 0.5) + 1):
        for y in range(1, int(limit ** 0.5) + 1):
            n = 4 * x ** 2 + y ** 2
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                sieve[n] = not sieve[n]
            n = 3 * x ** 2 + y ** 2
            if n <= limit and n % 12 == 7:
                sieve[n] = not sieve[n]
            n = 3 * x ** 2 - y ** 2
            if x > y and n <= limit and n % 12 == 11:
                sieve[n] = not sieve[n]

    for i in range(5, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i * i):
                sieve[j] = False

    return [2, 3] + [x for x in range(5, limit + 1) if sieve[x]]


# Алгоритм Миллера-Рабина
def miller_rabin(n, k=5):
    """
    Тест Миллера-Рабина для проверки простоты числа.

    :param n: Число для проверки.
    :param k: Количество раундов для повышения точности.
    :return: True, если n вероятно простое, False, если составное.
    """
    import random

    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    # Разложение n-1 на вид (2^r) * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Основная проверка
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True


def primes_miller_rabin(limit, k=5):
    """
    Нахождение всех простых чисел до limit с помощью теста Миллера-Рабина.

    :param limit: Граница поиска простых чисел.
    :param k: Количество раундов для повышения точности.
    :return: Список вероятно простых чисел.
    """
    primes = []
    for num in range(2, limit + 1):
        if miller_rabin(num, k):
            primes.append(num)
    return primes

