import copy

def print_all_sum_rec(target, current_sum, start, output, result):
    if current_sum is target:
        output.append(copy.copy(result))
    
    for i in range(start,target):
        temp_sum = current_sum + i
    
        if temp_sum <= target:
            result.append(i)
            print_all_sum_rec(target, temp_sum, i, output, result)
            result.pop()
        else:
            return
def print_all_sum(target):
    output = []
    result = []
    print_all_sum_rec(target, 0, 1, output, result)
    return output

def main():
    result = print_all_sum(2)
    print("1. All sum combinations of" + " 2: " + str(result))
    print("\n-----------------------------------------------------------------------------------------------------\n")
    result1 = print_all_sum(3)
    print("2. All sum combinations of" + " 3: " + str(result1))
    print("\n-----------------------------------------------------------------------------------------------------\n")
    result2 = print_all_sum(4)
    print("3. All sum combinations of" + " 4: " + str(result2))
    print("\n-----------------------------------------------------------------------------------------------------\n")
    result3 = print_all_sum(7)
    print("3. All sum combinations of" + " 7: " + str(result3))
    print("\n-----------------------------------------------------------------------------------------------------\n")



if __name__ == '__main__':
    main()