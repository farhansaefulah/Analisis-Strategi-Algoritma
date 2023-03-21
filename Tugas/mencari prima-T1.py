def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

n = 7
if is_prime(n):
    print(n, "adalah bilangan prima")
else:
    print(n, "bukan bilangan prima")
