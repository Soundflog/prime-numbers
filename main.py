import primes
import time

if __name__ == "__main__":
    limit = 100

    tic = time.perf_counter()
    print("Простые числа методом простой проверки делением:")
    print(primes.primes_basic(limit))
    print(f"Вычисление заняло: {time.perf_counter() - tic:0.4f} секунд")

    tic = time.perf_counter()
    print("\nПростые числа методом Решета Эратосфена:")
    print(primes.sieve_of_eratosthenes(limit))
    print(f"Вычисление заняло: {time.perf_counter() - tic:0.4f} секунд")

    tic = time.perf_counter()
    print("\nПростые числа методом Решета Аткина:")
    print(primes.sieve_of_atkin(limit))
    print(f"Вычисление заняло: {time.perf_counter() - tic:0.4f} секунд")

    tic = time.perf_counter()
    print("\nПростые числа методом теста Миллера-Рабина:")
    print(primes.primes_miller_rabin(limit))
    print(f"Вычисление заняло: {time.perf_counter() - tic:0.4f} секунд")
