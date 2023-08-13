def str_rev(_str, start,end):
    if _str == None or len(_str) < 2:
        return
    while start < end:
        _str[start], _str[end] = _str[end], _str[start]
        start += 1
        end -= 1
    return _str

def reverse_words(sentence):
    str_len = len(sentence)
    if sentence == None or str_len == 0:
        return ""
    str_rev(sentence, 0, str_len - 1)
    i = 0
    j = 0
    while i<str_len:
        while i < j or i < str_len and sentence[i] == " ":
            i += 1
        while j < i or j < str_len and sentence[j] != " ":
            j += 1
        str_rev(sentence, i, j - 1)
        i = j
    return sentence

def main():
    string_to_reverse1 = list("Hello World!")
    print("1.    Actual string:   " + "".join(string_to_reverse1))
    reverse_words(string_to_reverse1)
    print("      Reversed string: " + "".join(string_to_reverse1))
    print("-----------------------------------------------------------------------------------------------------")
    string_to_reverse2 = list("The quick brown fox jumped over the lazy dog.")
    print("2.    Actual string:   " + "".join(string_to_reverse2))
    reverse_words(string_to_reverse2)
    print("      Reversed string: " + ("".join(string_to_reverse2)))
    print("-----------------------------------------------------------------------------------------------------")


if __name__ == '__main__':
    main()