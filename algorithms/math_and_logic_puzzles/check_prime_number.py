import math


def check_prime_number(n):
    if n <= 1:
        return False
    sqrt = int(math.sqrt(n))
    for i in range(2, sqrt + 1):
        if n % i == 0:
            return False

    return True


if __name__ == "__main__":
    for i in range(10):
        print("{0} is prime number: {1}".format(i, check_prime_number(i)))
