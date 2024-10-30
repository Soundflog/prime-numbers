import time
import ctypes
from algorithms import is_prime_basic, sieve_eratosthenes  # Реализации на Python

# Загрузка библиотеки C
prime_lib = ctypes.CDLL('./lib/prime_lib.dll')

# Настройка типов для функций C
prime_lib.is_prime_basic.argtypes = [ctypes.c_int]
prime_lib.is_prime_basic.restype = ctypes.c_bool

prime_lib.sieve_eratosthenes.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
prime_lib.sieve_eratosthenes.restype = ctypes.POINTER(ctypes.c_int)

# Тестовые данные
prime_numbers = [1009, 104729, 1299709]  # Простые числа для проверки на простоту
limits = [100000, 500000, 1000000]  # Пределы для генерации простых чисел


# Функция для тестирования на Python
def test_is_prime_python(numbers):
    for number in numbers:
        start_time = time.time()
        result = is_prime_basic(number)
        elapsed_time = time.time() - start_time
        print(f"Python: Число {number} простое: {result}, время: {elapsed_time:.6f} секунд")


# Функция для тестирования на C
def test_is_prime_c(numbers):
    for number in numbers:
        start_time = time.time()
        result = prime_lib.is_prime_basic(number)
        elapsed_time = time.time() - start_time
        print(f"C: Число {number} простое: {result}, время: {elapsed_time:.6f} секунд")


# Функция для генерации простых чисел на Python
def test_generate_primes_python(limits):
    for limit in limits:
        start_time = time.time()
        sieve = sieve_eratosthenes(limit)
        primes = [i for i, is_prime in enumerate(sieve) if is_prime]
        elapsed_time = time.time() - start_time
        print(f"Python: Простые числа до {limit}, найдено {len(primes)}, время: {elapsed_time:.6f} секунд")


# Функция для генерации простых чисел на C
def test_generate_primes_c(limits):
    for limit in limits:
        prime_count = ctypes.c_int()
        start_time = time.time()
        primes_ptr = prime_lib.sieve_eratosthenes(limit, ctypes.byref(prime_count))
        primes = [primes_ptr[i] for i in range(prime_count.value)]
        elapsed_time = time.time() - start_time
        print(f"C: Простые числа до {limit}, найдено {len(primes)}, время: {elapsed_time:.6f} секунд")
        ctypes.CDLL("msvcrt.dll").free(primes_ptr)  # Освобождение памяти


# Запуск тестов
print("Сравнение проверки числа на простоту:")
test_is_prime_python(prime_numbers)
test_is_prime_c(prime_numbers)

print("\nСравнение генерации простых чисел:")
test_generate_primes_python(limits)
test_generate_primes_c(limits)
