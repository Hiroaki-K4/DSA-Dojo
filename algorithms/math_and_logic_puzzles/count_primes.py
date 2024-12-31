import math


# count primes less than n
def count_primes(n):
    if n < 2:
        return 0
    result = [True] * n
    result[0] = result[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if result[i]:
            for j in range(i + i, n, i):
                result[j] = False

    return sum(result)


if __name__ == "__main__":
    for i in range(10):
        print("Count primes {0}: {1}".format(i, count_primes(i)))
