from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import algorithms  # Импортируем модуль с алгоритмами для работы с простыми числами


# Ограничение разрешенных путей
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


# Создаем сервер
with SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler, allow_none=True) as server:
    server.register_introspection_functions()


    # Функция для проверки простоты числа
    def is_prime(number):
        return algorithms.is_prime_basic(number)


    # Функция для нахождения всех простых чисел до указанного предела
    def get_primes(limit):
        return [num for num in range(2, limit + 1) if algorithms.is_prime_basic(num)]


    # Регистрируем функции, которые могут вызываться клиентом
    server.register_function(is_prime, 'is_prime')
    server.register_function(get_primes, 'get_primes')

    # Запуск сервера
    print("Сервер запущен на порту 8000...")
    server.serve_forever()
