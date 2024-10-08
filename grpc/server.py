from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import algorithms  # Импортируем модуль с алгоритмами для работы с простыми числами


# Ограничение разрешенных путей
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


# Создаем сервер
with SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler, allow_none=True) as server:
    server.register_introspection_functions()


    # Функция для проверки простоты числа (метод деления)
    def is_prime_basic(number):
        return algorithms.is_prime_basic(number)


    # Функция для нахождения всех простых чисел до предела (метод Решета Эратосфена)
    def get_primes_eratosthenes(limit):
        sieve = algorithms.sieve_eratosthenes(limit)
        return [i for i in range(2, limit + 1) if sieve[i]]


    # Функция для нахождения всех простых чисел до предела (метод Решета Аткина)
    def get_primes_atkin(limit):
        sieve = algorithms.sieve_atkin(limit)
        return [i for i in range(2, limit + 1) if sieve[i]]


    # Функция для проверки числа на простоту (метод Миллера-Рабина)
    def is_prime_miller_rabin(number):
        return algorithms.miller_rabin(number)


    # Регистрируем функции, которые могут вызываться клиентом
    server.register_function(is_prime_basic, 'is_prime_basic')
    server.register_function(get_primes_eratosthenes, 'get_primes_eratosthenes')
    server.register_function(get_primes_atkin, 'get_primes_atkin')
    server.register_function(is_prime_miller_rabin, 'is_prime_miller_rabin')

    # Запуск сервера
    print("Сервер запущен на порту 8000...")
    server.serve_forever()
