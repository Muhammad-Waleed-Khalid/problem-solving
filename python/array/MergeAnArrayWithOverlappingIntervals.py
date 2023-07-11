class Interval:
  def __init__(self, first, second):
    self.first = first
    self.second = second
''' Here is the code for merging intervals. The time complexity is O(n) and the space complexity is O(1).'''''
def merge_intervals(v):
  result = [v[0]]
  j = 1
  for i in range(1,len(v)):
    if result[j-1].second >= v[i].first:
      if v[i].second > result[j-1].second:
        result[j-1].second = v[i].second

    else:
      result.append(v[i])
      j+=1
  return result


# Printing list of intervals
def print_interval_list(lst):
    result_str = ""
    for i in range(len(lst)):
        result_str += "[" + str(lst[i].first) + \
            ", " + str(lst[i].second) + "], "
    return result_str[:-2]


def main():
    v1 = [Interval(1, 5), Interval(3, 7), Interval(4, 6)]
    v2 = [Interval(1, 5), Interval(4, 6), Interval(6, 8), Interval(11, 15)]
    v3 = [Interval(3, 7), Interval(6, 8), Interval(10, 12), Interval(11, 15)]
    v4 = [Interval(1, 5)]

    v_list = [v1, v2, v3, v4]

    for i in range(len(v_list)):
        print(i + 1, end="")
        print(".\tIntervals to merge:\t " + print_interval_list(v_list[i])) 
        result = merge_intervals(v_list[i])
        print("\tMerged intervals:\t " + print_interval_list(result)) 
        print("----------------------------------------------------------------------------------------------------\n")


if __name__ == '__main__':
    main()