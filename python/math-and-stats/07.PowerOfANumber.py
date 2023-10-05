def pos_power(x,n):
  if n == 0:
    return 1
  if n == 1:
    return x
  if n % 2 == 0:
    return power(x*x,n//2)
  return x * power(x*x,n//2)

def power(x, n):
  if n<0:
    return 1/pos_power(x,-n)
  return pos_power(x,n)

def main():
    print("1. Power(0, 0) = %.3f" %power(0, 0))
    print("2. Power(2, 5) = %.3f" %power(2, 5))
    print("3. Power(3, 4) = %.3f" %power(3, 4))
    print("4. Power(1.5, 3) = %.3f" %power(1.5, 3))
    print("5. Power(2, -2) = %.3f" %power(2, -2))

if __name__ == '__main__':
    main()