'''Here is the code for finding the smallest common number between 3 arrays. The time complexity is O(n) and the space complexity is O(1).'''

def find_least_common_number(a, b, c):
    i = 0
    j = 0
    k = 0

    while i < len(a) and j < len(b) and k < len(c):

        # Finding the smallest common number
        if a[i] == b[j] and b[j] == c[k]:
            return a[i]

        # Let's increment the iterator
        # for the smallest value.

        if a[i] <= b[j] and a[i] <= c[k]:
            i += 1
        elif b[j] <= a[i] and b[j] <= c[k]:
            j += 1
        elif c[k] <= a[i] and c[k] <= b[j]:
            k += 1
    return -1

'''Here is the driver code for finding the smallest common number between 3 arrays. To test the algorithm,.'''''
def main():
    v1 = [1, 6, 7, 10, 25, 30, 63, 64]
    v2 = [0, 1, 2, 4, 5, 6, 7, 8, 50]
    v3 = [1, 6, 10, 14]
    print("Array 1: ", v1)
    print("Array 2: ", v2)
    print("Array 3: ", v3)
    result = find_least_common_number(v1, v2, v3)
    print("Least Common Number: " + str(result))


if __name__ == '__main__':
    main()