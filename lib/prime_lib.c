#include <stdbool.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>

// Простая проверка числа на простоту методом деления
bool is_prime_basic(int number) {
    if (number <= 1) return false;
    if (number == 2) return true;
    if (number % 2 == 0) return false;
    for (int i = 3; i <= sqrt(number); i += 2) {
        if (number % i == 0) return false;
    }
    return true;
}

// Решето Эратосфена для генерации всех простых чисел до предела
int* sieve_eratosthenes(int limit, int* prime_count) {
    bool* sieve = (bool*)malloc((limit + 1) * sizeof(bool));
    for (int i = 0; i <= limit; i++) sieve[i] = true;
    sieve[0] = sieve[1] = false;

    for (int i = 2; i <= sqrt(limit); i++) {
        if (sieve[i]) {
            for (int j = i * i; j <= limit; j += i) sieve[j] = false;
        }
    }

    *prime_count = 0;
    for (int i = 2; i <= limit; i++) {
        if (sieve[i]) (*prime_count)++;
    }

    int* primes = (int*)malloc((*prime_count) * sizeof(int));
    int index = 0;
    for (int i = 2; i <= limit; i++) {
        if (sieve[i]) primes[index++] = i;
    }

    free(sieve);
    return primes;
}

// Решето Аткина для генерации всех простых чисел до предела
int* sieve_atkin(int limit, int* prime_count) {
    bool* sieve = (bool*)calloc(limit + 1, sizeof(bool));
    sieve[2] = sieve[3] = true;

    for (int x = 1; x * x <= limit; x++) {
        for (int y = 1; y * y <= limit; y++) {
            int n = 4 * x * x + y * y;
            if (n <= limit && (n % 12 == 1 || n % 12 == 5)) sieve[n] = !sieve[n];
            n = 3 * x * x + y * y;
            if (n <= limit && n % 12 == 7) sieve[n] = !sieve[n];
            n = 3 * x * x - y * y;
            if (x > y && n <= limit && n % 12 == 11) sieve[n] = !sieve[n];
        }
    }

    for (int i = 5; i * i <= limit; i++) {
        if (sieve[i]) {
            for (int j = i * i; j <= limit; j += i * i) sieve[j] = false;
        }
    }

    *prime_count = 0;
    for (int i = 2; i <= limit; i++) {
        if (sieve[i]) (*prime_count)++;
    }

    int* primes = (int*)malloc((*prime_count) * sizeof(int));
    int index = 0;
    for (int i = 2; i <= limit; i++) {
        if (sieve[i]) primes[index++] = i;
    }

    free(sieve);
    return primes;
}

// Тест Миллера-Рабина
bool miller_rabin(int n, int k) {
    if (n <= 1) return false;
    if (n == 2 || n == 3) return true;
    if (n % 2 == 0) return false;

    int r = 0;
    int d = n - 1;
    while (d % 2 == 0) {
        d /= 2;
        r++;
    }

    srand(time(NULL));
    for (int i = 0; i < k; i++) {
        int a = 2 + rand() % (n - 3);
        int x = (int)pow(a, d) % n;
        if (x == 1 || x == n - 1) continue;

        int j;
        for (j = 0; j < r - 1; j++) {
            x = (x * x) % n;
            if (x == n - 1) break;
        }

        if (j == r - 1) return false;
    }
    return true;
}
