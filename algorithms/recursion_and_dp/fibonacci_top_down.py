def fibonacci_memo(i, memo):
    if i == 0 or i == 1:
        return i
    if memo[i] == 0:
        memo[i] = fibonacci_memo(i - 1, memo) + fibonacci_memo(i - 2, memo)
    return memo[i]


def fibonacci(n):
    memo = [0] * (n + 1)
    return fibonacci_memo(n, memo)


if __name__ == "__main__":
    n = 0
    print("fib({0}) -> {1}".format(n, fibonacci(n)))
    n = 1
    print("fib({0}) -> {1}".format(n, fibonacci(n)))
    n = 5
    print("fib({0}) -> {1}".format(n, fibonacci(n)))
    n = 50
    print("fib({0}) -> {1}".format(n, fibonacci(n)))
