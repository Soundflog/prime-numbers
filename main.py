import primes


if __name__ == "__main__":
    limit = 100

    print("Простые числа методом простой проверки делением:")
    print(primes.primes_basic(limit))

    print("\nПростые числа методом Решета Эратосфена:")
    print(primes.sieve_of_eratosthenes(limit))

    print("\nПростые числа методом Решета Аткина:")
    print(primes.sieve_of_atkin(limit))

    print("\nПростые числа методом сегментированного Решета Эратосфена:")
    print(primes.segmented_sieve(limit))
