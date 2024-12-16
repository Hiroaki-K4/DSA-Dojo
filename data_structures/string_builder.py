import time


def slow_string_builder(str_list):
    merged = ""
    for s in str_list:
        merged += s

    return merged


def fast_string_builder(str_list):
    return "".join(str_list)


if __name__ == "__main__":
    str_list = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQR", "STU", "VRX", "YZ"]
    start = time.time()
    merged = slow_string_builder(str_list)
    print("Time: {0}[s], Result: {1}".format(time.time() - start, merged))

    start = time.time()
    merged = fast_string_builder(str_list)
    print("Time: {0}[s], Result: {1}".format(time.time() - start, merged))
