def find_missing(arr):
    n  = len(arr)
    s = n*(n+1)//2
    for i in arr:
        s -= i
    return s

def main():
    v_list = [[0], [3,7,1,2,0,4,5], [9,6,4,2,3,5,7,0,1]]
    
    for i in range(len(v_list)):
        print("1. Original:", v_list[i])
        missing_number = find_missing(v_list[i])
        print("   The missing number is: " + str(missing_number))
        print("-" * 100)
    
if __name__ == '__main__':
    main()