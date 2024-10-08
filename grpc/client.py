import xmlrpc.client

# Создаем подключение к серверу
server = xmlrpc.client.ServerProxy('http://localhost:8000')

# Пример использования функции проверки числа на простоту
number = 29
is_prime = server.is_prime(number)
print(f"Число {number} является простым: {is_prime}")

# Пример использования функции для нахождения всех простых чисел до предела
limit = 100
primes = server.get_primes(limit)
print(f"Простые числа до {limit}: {primes}")
