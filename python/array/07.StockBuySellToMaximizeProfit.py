'''Here is  the code for finding the maximum profit that can be made by buying and selling a stock. The time complexity is O(n) and the space complexity is O(1).'''
def find_buy_sell_stock_prices(array):
    if array == None or len(array) < 2:
        return None
    current_buy = array[0]
    global_sell = array[1]
    global_profit = global_sell - current_buy
    current_profit = float('-inf')
    for i in range(1, len(array)):
        current_profit = array[i] - current_buy
        if current_profit > global_profit:
            global_profit = current_profit
            global_sell = array[i]
        if current_buy > array[i]:
            current_buy = array[i]
    result = global_sell - global_profit, global_sell
    return result


'''Here is the driver code for finding the maximum profit that can be made by buying and selling a stock. To test the algorithm.'''
def main():
    stock_prices_data = [[1, 2, 3, 4, 3, 2, 1, 2, 5], [
        8, 6, 5, 4, 3, 2, 1], [12, 30, 40, 90, 110], [2]]

    for i in range(len(stock_prices_data)):
        result = find_buy_sell_stock_prices(stock_prices_data[i])
        print(str(i + 1) + ". Day stocks:", stock_prices_data[i])
        if result is not None:
            print("   Buy Price: " +
                  str(result[0]) + ", Sell Price: " + str(result[1]))
        else:
            print("   Buy Price: None, Sell Price: None")
        print("-------------------------------------------------------------------------------------------------------\n")


if __name__ == '__main__':
    main()