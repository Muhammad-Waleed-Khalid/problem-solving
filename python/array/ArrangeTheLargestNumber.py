class LargerNumKey(str):
  def __lt__(x,y):
    return x+y > y+x

def largest_number(nums):
  mapStr = map(str, nums)
  mapStr = sorted(mapStr,key=LargerNumKey)
  largest = ''.join(mapStr)

  return '0' if largest[0] == '0' else largest


def main():
     # Driver Code
    nums_arr = [[21,35,20], [0, 5, 1, 3, 2, 4], [71, 5, 21, 52], [0, 0, 0], [1]]
    
    for i in range(len(nums_arr)):
        print(str(i+1) + ". The largest possible number obtained by arranging", nums_arr[i], "is: '", end = "")
        print(str(largest_number(nums_arr[i])) + "'")
        print("---------------------------------------------------------------------------------------------------------------------\n")

if __name__ == '__main__':
    main()