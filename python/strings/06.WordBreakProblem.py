def can_segment_string(inputString, dictionary):
  if not inputString:
    return True
  for i in range(1, len(inputString) + 1):
    first = inputString[0:i]
    if first in dictionary:
      second = inputString[i:]
      if second in dictionary:
        return True
      if can_segment_string(second, dictionary):
        return True
  return False
def main():
    input_string = ["hellonow", "nowok", "applepie", "applejuice"]
    words_dictionary = [["hello", "hell", "on", "now"], ["hello", "hell", "on", "now"], [
        "apple", "pear", "pier", "pie"], ["apple", "pear", "pier", "pie"]]

    for i in range(len(input_string)):
        print(str(i+1) + ". Words dictionary: " +
              str(words_dictionary[i]).replace("'", '"'))
        print("   Input string: "+input_string[i])

        if can_segment_string(input_string[i], words_dictionary[i]):
            print("   Result: String can be segmented")
        else:
            print("   Result: String can not be segmented")
        print("---------------------------------------------------------------------------------------------------\n")


if __name__ == '__main__':
    main()