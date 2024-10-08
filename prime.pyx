cdef extern from "prime.c":
    bint is_prime(int n)

def check_prime(int n):
    """Обертка для вызова C-функции is_prime в Python."""
    return is_prime(n)
