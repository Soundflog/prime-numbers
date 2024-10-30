import xmlrpc.client

# Подключение к серверу
server = xmlrpc.client.ServerProxy('http://localhost:8000')

# Проверка числа на простоту
number = 29
is_prime = server.is_prime_basic(number)
print(f"Число {number} является простым: {is_prime}")

# Нахождение всех простых чисел до заданного предела (Решето Эратосфена)
limit = 100
primes_eratosthenes = server.get_primes_eratosthenes(limit)
print(f"Простые числа до {limit} (Решето Эратосфена): {primes_eratosthenes}")

# Нахождение всех простых чисел до заданного предела (Решето Аткина)
primes_atkin = server.get_primes_atkin(limit)
print(f"Простые числа до {limit} (Решето Аткина): {primes_atkin}")

# Проверка числа на простоту (Тест Миллера-Рабина)
is_prime_mr = server.is_prime_miller_rabin(number, 5)
print(f"Тест Миллера-Рабина: Число {number} является простым: {is_prime_mr}")