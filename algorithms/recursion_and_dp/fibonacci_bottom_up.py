def fibonacci(n):
    if n == 0 or n == 1:
        return n
    memo = [0] * n
    memo[0] = 0
    memo[1] = 1
    for i in range(2, n):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n - 1] + memo[n - 2]


if __name__ == "__main__":
    n = 0
    print("fib({0}) -> {1}".format(n, fibonacci(n)))
    n = 1
    print("fib({0}) -> {1}".format(n, fibonacci(n)))
    n = 5
    print("fib({0}) -> {1}".format(n, fibonacci(n)))
    n = 50
    print("fib({0}) -> {1}".format(n, fibonacci(n)))
