def dict_to_lst(subset):
    result = []
    if subset == []:
        return [[]]
    for dic in subset:
        result.append(list(dic))
    return result

def find_all_subsets(v, sets):
    l = len(v)
    n = 2**l
    for i in range(0,n):
        st = set()
        for j in range(l):
            w = 1 << j
            if i & w != 0:
                st.add(v[j])
        sets.append(st)
    return sets


def main():
    v = [[], [2, 5, 7], [1, 2], [1, 2, 3, 4]]

    for i in range(len(v)):
        subsets = []
        find_all_subsets(v[i], subsets)
        print(i + 1, ". Set:     ", v[i], sep='')

        print("   Subsets:", dict_to_lst(subsets))
        print("-"*100)

if __name__ == '__main__':
    main()
