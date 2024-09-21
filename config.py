from algorithms import is_prime_basic, sieve_eratosthenes, sieve_atkin, miller_rabin


def find_primes(entry_limit, algorithm_var, result_text):
    """Функция для поиска всех простых чисел до заданного предела."""
    try:
        limit = int(entry_limit.get())
        if limit < 2:
            result_text.set("Введите число больше 1.")
            return

        # Выбор алгоритма для поиска простых чисел
        selected_algorithm = algorithm_var.get()
        if selected_algorithm == "Простая проверка":
            primes = [i for i in range(2, limit + 1) if is_prime_basic(i)]
        elif selected_algorithm == "Решето Эратосфена":
            sieve = sieve_eratosthenes(limit)
            primes = [i for i in range(2, limit + 1) if sieve[i]]
        elif selected_algorithm == "Решето Аткина":
            sieve = sieve_atkin(limit)
            primes = [i for i in range(2, limit + 1) if sieve[i]]
        elif selected_algorithm == "Тест Миллера-Рабина":
            primes = [i for i in range(2, limit + 1) if miller_rabin(i)]
        else:
            result_text.set("Неизвестный алгоритм.")
            return

        result_text.set(f"Простые числа до {limit}: {primes}")

    except ValueError:
        result_text.set("Введите корректное целое число.")


def check_prime(entry_number, algorithm_var, result_text):
    """Функция для проверки числа на простоту."""
    try:
        number = int(entry_number.get())
        if number < 2:
            result_text.set("Введите число больше 1.")
            return

        # Выбор алгоритма для проверки числа
        selected_algorithm = algorithm_var.get()
        if selected_algorithm == "Простая проверка":
            is_prime = is_prime_basic(number)
        elif selected_algorithm == "Решето Эратосфена":
            sieve = sieve_eratosthenes(number)
            is_prime = sieve[number]
        elif selected_algorithm == "Решето Аткина":
            sieve = sieve_atkin(number)
            is_prime = sieve[number]
        elif selected_algorithm == "Тест Миллера-Рабина":
            is_prime = miller_rabin(number)
        else:
            result_text.set("Неизвестный алгоритм.")
            return

        result_text.set(f"{number} является простым: {is_prime}")

    except ValueError:
        result_text.set("Введите корректное целое число.")
