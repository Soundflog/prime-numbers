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


# Модифицированное Решето Эратосфена с сегментацией
def segmented_sieve(limit):
    """Модифицированное Решето Эратосфена с сегментацией."""
    import math

    def simple_sieve(limit, primes):
        sieve = [True] * (limit + 1)
        for p in range(2, limit + 1):
            if sieve[p]:
                primes.append(p)
                for i in range(p * p, limit + 1, p):
                    sieve[i] = False

    segment_size = int(math.sqrt(limit)) + 1
    primes = []
    simple_sieve(segment_size, primes)

    low = segment_size
    high = 2 * segment_size
    prime_list = primes[:]

    while low < limit:
        if high >= limit:
            high = limit + 1

        sieve = [True] * (high - low)

        for prime in primes:
            low_lim = max(prime * prime, (low + prime - 1) // prime * prime)
            for j in range(low_lim, high, prime):
                sieve[j - low] = False

        for i in range(low, high):
            if sieve[i - low]:
                prime_list.append(i)

        low = low + segment_size
        high = high + segment_size

    return prime_list
