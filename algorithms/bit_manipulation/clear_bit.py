def clear_bit(num, i):
    mask = ~(1 << i)
    return num & mask


def clear_bits_MSB_throughI(num, i):
    mask = (1 << i) - 1
    return num & mask


def clear_bits_Ithrough0(num, i):
    mask = -1 << (i + 1)
    return num & mask


if __name__ == "__main__":
    num = 42
    i_0 = 3
    i_1 = 2

    print(
        "num = {0}, i = {1}, clear_bit = {2}".format(num, i_0, clear_bit(num, i_0))
    )  # 34
    print(
        "num = {0}, i = {1}, clear_bit = {2}".format(num, i_1, clear_bit(num, i_1))
    )  # 42

    print(
        "num = {0}, i = {1}, clear_bits_MSB_throughI = {2}".format(
            num, i_0, clear_bits_MSB_throughI(num, i_0)
        )
    )  # 2
    print(
        "num = {0}, i = {1}, clear_bits_MSB_throughI = {2}".format(
            num, i_1, clear_bits_MSB_throughI(num, i_1)
        )
    )  # 2

    print(
        "num = {0}, i = {1}, clear_bits_Ithrough0 = {2}".format(
            num, i_0, clear_bits_Ithrough0(num, i_0)
        )
    )  # 32
    print(
        "num = {0}, i = {1}, clear_bits_Ithrough0 = {2}".format(
            num, i_1, clear_bits_Ithrough0(num, i_1)
        )
    )  # 40
