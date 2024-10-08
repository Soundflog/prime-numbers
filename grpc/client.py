import xmlrpc.client

# Создаем подключение к серверу
server = xmlrpc.client.ServerProxy('http://localhost:8000')

# Пример использования функции проверки числа на простоту (метод деления)
number = 29
is_prime = server.is_prime_basic(number)
print(f"Метод деления: число {number} является простым: {is_prime}")

# Пример использования функции для нахождения всех простых чисел до предела (Решето Эратосфена)
limit = 100
primes_eratosthenes = server.get_primes_eratosthenes(limit)
print(f"Решето Эратосфена: Простые числа до {limit}: {primes_eratosthenes}")

# Пример использования функции для нахождения всех простых чисел до предела (Решето Аткина)
primes_atkin = server.get_primes_atkin(limit)
print(f"Решето Аткина: Простые числа до {limit}: {primes_atkin}")

# Пример использования функции проверки числа на простоту (Тест Миллера-Рабина)
number = 104729
is_prime_miller_rabin = server.is_prime_miller_rabin(number)
print(f"Тест Миллера-Рабина: число {number} является простым: {is_prime_miller_rabin}")
