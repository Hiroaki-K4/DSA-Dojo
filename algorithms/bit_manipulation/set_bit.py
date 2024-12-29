def set_bit(num, i):
    return num | (1 << i)


if __name__ == "__main__":
    num = 42
    i = 3
    print("num = {0}, i = {1}, set_bit = {2}".format(num, i, set_bit(num, i)))
    i = 2
    print("num = {0}, i = {1}, set_bit = {2}".format(num, i, set_bit(num, i)))
