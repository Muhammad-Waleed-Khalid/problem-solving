def verify_alien_dictionary(words, order):
  keymap = {}
  for i in range(len(order)):
    keymap[order[i]] = i
  for i in range(len(words)-1):
    for j in range(len(words[i])):
      if j >= len(words[i+1]):
        return False
      if keymap[words[i][j]] != keymap[words[i+1][j]]:
        if keymap[words[i][j]] > keymap[words[i+1][j]]:
          return False
        else:
          break
  return True


# Driver Code
def main():
    # Example - 1
    words = ["alpha", "bravo", "charlie", "delta"]
    order = "abcdlpite"
    print("1. words = "  + str(words))
    print("   order = '" + order + "'")
    print("   Is the dictionary valid? " + ("Yes" if (verify_alien_dictionary(words, order)) else "No"))
    print("---------------------------------------------------------------------------------------------------\n")

    # Example - 2
    words2 = ["apple", "app"]
    order = "apple"
    print("2. words = " + str(words2))
    print("   order = '" + order + "'")
    print("   Is the dictionary valid? " + ("Yes" if (verify_alien_dictionary(words2, order)) else "No" ))
    print("---------------------------------------------------------------------------------------------------\n")

if __name__ == "__main__":
    main()