def remove_duplicates(_str):
    ch = set()
    _res = ""
    for i in _str:
        if i in ch:
            continue
        ch.add(i)
        _res+=i
    return _res

def main():
    str_list = ["dabbac", "aabbbccdddeee", "abcdef"]
    for i in range(len(str_list)):
        print(str(i+1) + ".     Before: ", str_list[i])
        str_list[i] = list(str_list[i])
        result = remove_duplicates(str_list[i])
        print("       After:  ", ''.join(result))
        print("-"*100)

if __name__ == '__main__':
    main()