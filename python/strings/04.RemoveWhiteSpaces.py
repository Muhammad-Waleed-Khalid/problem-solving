def remove_white_spaces (s):
  i = 0
  l = len(s)
  while i < l:
    if s[i] == ' ' or s[i] == '\t':
      del s[i]
      l-=1
    i+=1
  return ''.join(s) 

def main():
    str_list = ["All greek to me.", "We love Python", "You are amazing"]
    for i in range(len(str_list)):
      print(str(i+1) + ".     Actual string:                ", str_list[i])
      arr1 = list(str_list[i])
      print("       String without spaces or tabs:", remove_white_spaces(arr1))
      print("-" * 100)

if __name__ == '__main__':
    main()