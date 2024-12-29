def get_bit(num, i):
    return (num & (1 << i)) != 0


if __name__ == "__main__":
    num = 42
    i = 3
    print("{0}'s {1}-th bit is 1: {2}".format(num, i, get_bit(num, i)))
    i = 2
    print("{0}'s {1}-th bit is 1: {2}".format(num, i, get_bit(num, i)))
