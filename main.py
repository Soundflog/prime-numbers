import tkinter as tk
from config import find_primes, check_prime


def main():
    root = tk.Tk()
    root.title("Нахождение простых чисел и проверка")

    # Поле для ввода предела
    label_limit = tk.Label(root, text="Введите предел для поиска простых чисел:")
    label_limit.pack()
    entry_limit = tk.Entry(root)
    entry_limit.pack()

    # Поле для ввода числа для проверки
    label_number = tk.Label(root, text="Введите число для проверки на простоту:")
    label_number.pack()
    entry_number = tk.Entry(root)
    entry_number.pack()

    # Выбор алгоритма
    algorithm_var = tk.StringVar(value="Простая проверка")
    label_algorithm = tk.Label(root, text="Выберите алгоритм:")
    label_algorithm.pack()

    radio_basic = tk.Radiobutton(root, text="Простая проверка", variable=algorithm_var, value="Простая проверка")
    radio_basic.pack()

    radio_eratosthenes = tk.Radiobutton(root, text="Решето Эратосфена", variable=algorithm_var,
                                        value="Решето Эратосфена")
    radio_eratosthenes.pack()

    radio_atkin = tk.Radiobutton(root, text="Решето Аткина", variable=algorithm_var, value="Решето Аткина")
    radio_atkin.pack()

    radio_miller_rabin = tk.Radiobutton(root, text="Тест Миллера-Рабина", variable=algorithm_var,
                                        value="Тест Миллера-Рабина")
    radio_miller_rabin.pack()

    # Кнопка для поиска простых чисел
    btn_find_primes = tk.Button(root, text="Найти простые числа",
                                command=lambda: find_primes(entry_limit, algorithm_var, result_text))
    btn_find_primes.pack()

    # Поле для вывода результата поиска простых чисел
    result_text = tk.Text(root, height=10, width=50)
    result_text.pack()

    # Кнопка для проверки числа на простоту
    btn_check_prime = tk.Button(root, text="Проверить число на простоту",
                                command=lambda: check_prime(entry_number, algorithm_var))
    btn_check_prime.pack()

    # Запуск главного цикла приложения
    root.mainloop()


if __name__ == "__main__":
    main()
