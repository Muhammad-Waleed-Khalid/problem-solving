def divide_integer(dividend, divisor):
    if divisor == 0:
        return -1
    if dividend < divisor:
        return 0
    if dividend == divisor:
        return 1
    q = 1
    val = divisor
    while val < (dividend>>1):
        val <<= 1
        q <<= 1
    return q + divide_integer(dividend-val, divisor)


def main():
    print("1. 7/2 =", divide_integer(7, 2))
    print("-----------------------------------------------------------------------------------------------------\n")
    print("2. 5/4 =", divide_integer(5, 4))
    print("-----------------------------------------------------------------------------------------------------\n")
    print("3. 1/3 =", divide_integer(1, 3))
    print("-----------------------------------------------------------------------------------------------------\n")
    print("4. 40/5 =", divide_integer(40, 5))
    print("-----------------------------------------------------------------------------------------------------\n")
    print("5. 40/4 =", divide_integer(40, 4))
    print("-----------------------------------------------------------------------------------------------------\n")


if __name__ == '__main__':
    main()