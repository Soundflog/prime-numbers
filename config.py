import tkinter as tk
from tkinter import messagebox
from algorithms.limit_primes_number import primes_basic, sieve_of_eratosthenes, sieve_of_atkin, primes_miller_rabin
from algorithms.primes_single_number import is_prime_basic_single, sieve_of_eratosthenes_single, sieve_of_atkin_single, miller_rabin_single


def find_primes(entry_limit, algorithm_var, result_text):
    """Функция для поиска всех простых чисел до заданного предела."""
    try:
        limit = int(entry_limit.get())
        if limit < 2:
            messagebox.showerror("Ошибка", "Введите число больше 1.")
            return

        # Выбор алгоритма для поиска
        selected_algorithm = algorithm_var.get()
        if selected_algorithm == "Простая проверка":
            result = primes_basic(limit)
        elif selected_algorithm == "Решето Эратосфена":
            result = sieve_of_eratosthenes(limit)
        elif selected_algorithm == "Решето Аткина":
            result = sieve_of_atkin(limit)
        elif selected_algorithm == "Тест Миллера-Рабина":
            result = primes_miller_rabin(limit)

        # Вывод результата
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, ", ".join(map(str, result)))

    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите корректное целое число.")


def check_prime(entry_number, algorithm_var):
    """Функция для проверки, является ли число простым."""
    try:
        number = int(entry_number.get())
        if number < 2:
            messagebox.showinfo("Результат", f"{number} не является простым числом.")
            return

        # Выбор алгоритма для проверки
        selected_algorithm = algorithm_var.get()
        if selected_algorithm == "Простая проверка":
            result = is_prime_basic_single(number)
        elif selected_algorithm == "Решето Эратосфена":
            result = sieve_of_eratosthenes_single(number)
        elif selected_algorithm == "Решето Аткина":
            result = sieve_of_atkin_single(number)
        elif selected_algorithm == "Тест Миллера-Рабина":
            result = miller_rabin_single(number)

        # Отображение результата
        if result:
            messagebox.showinfo("Результат", f"{number} является простым числом.")
        else:
            messagebox.showinfo("Результат", f"{number} не является простым числом.")

    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите корректное целое число.")
