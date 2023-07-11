'''Here is code of sorting colors in an array. The time complexity is O(n) and the space complexity is O(n).'''
def sort_colors (arr):
    hashmap = {0:0,1:0,2:0}
    for i in arr:
        hashmap[i]+=1
    j=0
    for i in hashmap:
       while hashmap[i]>0:
           arr[j]=i
           j+=1
           hashmap[i]-=1
    return arr 
''' Here is code of sorting colors in an array. The time complexity is O(n) and the space complexity is O(1).'''
def sort_colors_without_extra_space(arr):
    l = len(arr)
    i = 0
    j = l-1
    k = 0
    while k<=j:
        if arr[k]==0:
            arr[i],arr[k] = arr[k],arr[i]
            i+=1
            k+=1
        elif arr[k]==2:
            arr[j],arr[k] = arr[k],arr[j]
            j-=1
        else:
            k+=1
    return arr

''' Here is the driver code for sorting colors in an array. To test the algorithm'''


def main():
    input_list = [[2,0,2,1,1,0], [2,0,1],[2,0,2,1,1,0,1,0,1,0,2]]
    for i in range(len(input_list)):
        print(str(i+1) + ". Unsorted colors:" , input_list[i])
        sort_colors(input_list[i])
        print("   Sorted colors:  ", input_list[i])
        print("-"*100)
        print(str(i+1) + ". Unsorted colors:" , input_list[i])
        sort_colors_without_extra_space(input_list[i])
        print("   Sorted colors without extra Space:  ", input_list[i])
        print("-"*100)
        
if __name__ == "__main__":
    main()