def pythagorean_sum(a, b, c):
    if a>b and a>c:
        c, a = a, c
    elif b>a and b>c:
        c, b = b, c
    return a**2 + b**2 - c**2



def find_pythagorean_triples(arr):
    triples = []
    arr.sort()
    n = len(arr)
    for i in range(0,n):
        if arr[i] == 0:
            continue
        c = arr[i]**2
        j = 0
        k = n-1
        while j<k:
            if j==i or arr[j]==0:
                j += 1
                continue
            if k==i or arr[k]==0:
                k -= 1
                continue
            a = arr[j]**2
            b = arr[k]**2
            if a+b == c:
                triples.append([arr[j], arr[k], arr[i]])
            
            if a+b > c:
                k -= 1
            else:
                j += 1

          
    return triples


def main():
  pythagorean_list = [[4,16,1,2,3,5,6,8,25,10], [3,4,5,10,12,13,14,14,15],[2, 4, 6, 8, 10, 12, 14, 16, 18, 20],[1, 2, 3, 44, 5],[3, -1, 2, 5, 4]]
  for i in range(len(pythagorean_list)):
    result = find_pythagorean_triples(pythagorean_list[i])
    print("1.  Original:             ", pythagorean_list[i])
    print("    Pythagorean triples:  ", result)
    print("-"*100)

if __name__ == '__main__':
    main()