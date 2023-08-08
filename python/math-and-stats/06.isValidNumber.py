def is_number_valid(s):
  dot = 0
  for i in range(len(s)):
    if s[i] == '.':
      dot += 1
      if dot>1:
        return False
    elif s[i] == '-':
      if i==0:
        continue
      else:
        return False
    elif s[i]<'0' or s[i]>'9':
      return False
  return True


def main():
    print("Is the number valid 4.325?  ",
          "Yes" if is_number_valid("4.325") else "No")
    print("Is the number valid 1.1.1?  ",
          "Yes" if is_number_valid("1.1.1") else "No")
    print("Is the number valid 222?    ",
          "Yes" if is_number_valid("222") else "No")
    print("Is the number valid 22.?    ",
          "Yes" if is_number_valid("22.") else "No")
    print("Is the number valid 0.1?    ",
          "Yes" if is_number_valid("0.1") else "No")
    print("Is the number valid 22.22.? ",
          "Yes" if is_number_valid("22.22.") else "No")
    print("Is the number valid 1.?     ",
          "Yes" if is_number_valid("1.") else "No")


if __name__ == '__main__':
    main()
