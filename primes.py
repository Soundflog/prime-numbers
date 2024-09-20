def is_prime(n):
    """Проверяет, является ли число простым."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def primes_up_to(n):
    """Возвращает список всех простых чисел до n включительно."""
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes


def primes_in_range(start, end):
    """Возвращает список простых чисел в диапазоне от start до end включительно."""
    primes = []
    for i in range(start, end + 1):
        if is_prime(i):
            primes.append(i)
    return primes


def prime_factors(n):
    """Возвращает список простых множителей числа n."""
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors
