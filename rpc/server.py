from xmlrpc.server import SimpleXMLRPCServer
from ctypes import CDLL, POINTER, c_int, c_bool, byref
import ctypes

# Загрузка библиотеки
prime_lib = CDLL('../lib/prime_lib.dll')

# Загрузка функции free из стандартной библиотеки C
libc = ctypes.CDLL("msvcrt.dll")  # Для Windows
libc.free.argtypes = [ctypes.c_void_p]

# Настройка типов и возвращаемых значений функций C
prime_lib.is_prime_basic.argtypes = [c_int]
prime_lib.is_prime_basic.restype = c_bool

prime_lib.sieve_eratosthenes.argtypes = [c_int, POINTER(c_int)]
prime_lib.sieve_eratosthenes.restype = POINTER(c_int)

prime_lib.sieve_atkin.argtypes = [c_int, POINTER(c_int)]
prime_lib.sieve_atkin.restype = POINTER(c_int)

prime_lib.miller_rabin.argtypes = [c_int, c_int]
prime_lib.miller_rabin.restype = c_bool


# Функция для проверки простоты числа (делением)
def is_prime_basic(number):
    return prime_lib.is_prime_basic(number)


# Функция для генерации простых чисел (Решето Эратосфена)
def get_primes_eratosthenes(limit):
    prime_count = c_int()
    primes_ptr = prime_lib.sieve_eratosthenes(limit, byref(prime_count))
    primes = [primes_ptr[i] for i in range(prime_count.value)]
    libc.free(primes_ptr)  # освобождаем память
    return primes


# Функция для генерации простых чисел (Решето Аткина)
def get_primes_atkin(limit):
    prime_count = c_int()
    primes_ptr = prime_lib.sieve_atkin(limit, byref(prime_count))
    primes = [primes_ptr[i] for i in range(prime_count.value)]
    libc.free(primes_ptr)  # освобождаем память
    return primes


# Функция для проверки числа (Тест Миллера-Рабина)
def is_prime_miller_rabin(number, k=5):
    return prime_lib.miller_rabin(number, k)


# Создаем сервер XML-RPC
with SimpleXMLRPCServer(('localhost', 8000)) as server:
    server.register_function(is_prime_basic, 'is_prime_basic')
    server.register_function(get_primes_eratosthenes, 'get_primes_eratosthenes')
    server.register_function(get_primes_atkin, 'get_primes_atkin')
    server.register_function(is_prime_miller_rabin, 'is_prime_miller_rabin')
    print("Сервер запущен на порту 8000...")
    server.serve_forever()
