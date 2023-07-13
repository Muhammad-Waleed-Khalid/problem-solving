'''Here is the code for finding the maximum water area in a container. The time complexity is O(n) and the space complexity is O(1).'''
def max_water_area_container(height):
    i = 0
    j = len(height)-1
    max_water = 0
    while(i<j):
        hi,hj= height[i],height[j]
        container = min(hi,hj)* (j-i)
        if max_water < container:
            max_water = container
        if hi < hj:
            i+=1
        else:
            j-=1
    return max_water

'''Driver code for finding the maximum water area in a container. To test the algorithm'''

def main():
    input_list = [
                [1, 8, 6, 2, 5, 4, 8, 3, 7], 
                [20, 30, 9, 69],
                [13, 18, 12, 8],
                [45, 32, 56, 99], [23, 20]
                ]
    index = 1
    for input in input_list:
        print(str(index) + ". max_water_area_container(" + str(input) + "): " + str(max_water_area_container(input)))
        index += 1
        print("----------------------------------------------------------------------------------------------------\n")

if __name__ == "__main__":
    main()