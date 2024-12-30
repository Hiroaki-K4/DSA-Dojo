def update_bit(num, i, is_bit_1):
    value = 1 if is_bit_1 else 0
    mask = ~(1 << i)
    return (num & mask) | (value << i)


if __name__ == "__main__":
    num = 42
    i_0 = 3
    i_1 = 2

    print(
        "num = {0}, i = {1}, is_bit_1 = {2}, update_bit = {3}".format(
            num, i_0, True, update_bit(num, i_0, True)
        )
    )  # 42

    print(
        "num = {0}, i = {1}, is_bit_1 = {2}, update_bit = {3}".format(
            num, i_1, True, update_bit(num, i_1, True)
        )
    )  # 46
