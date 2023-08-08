EP = 0.00001

def square_root(n):
    is_negative = False
    if n < 0:
        is_negative = True
        n = -n
    low = 0
    high = n
    guess = (low + high) / 2
    while abs(guess * guess - n) >= EP:
        if guess * guess > n:
            high = guess
        else:
            low = guess
        guess = (low + high) / 2
    if is_negative:
        return str(guess)+"i"
    return guess

def main():
    arr = [-16, 16, 17, 2.25]
    for i in range(len(arr)):
        ans = square_root(arr[i])
        ans_str = str(ans)
        print(str(i + 1) + ".   Square root of " +
              str(arr[i]) + ": " + str(ans_str))
        print("-"*100)


if __name__ == '__main__':
    main()