## 1. Серверное приложение:

* Открывает сервер на локальном хосте на порту 8000.
* Реализует две функции:
  * is_prime(number) — проверяет, является ли число простым.
  * get_primes(limit) — возвращает список всех простых чисел до указанного предела.
* Функции регистрируются на сервере, чтобы их можно было вызывать удалённо.


## 2. Клиентское приложение:

* Подключается к серверу через XML-RPC.
* Вызывает удалённые функции на сервере:
  * Проверка числа на простоту.
  * Нахождение всех простых чисел до указанного предела.

# Запуск
1. Запустите серверное приложение:
```bash
python server.py
```

2. Запустите клиентское приложение:
```bash
python client.py
```
