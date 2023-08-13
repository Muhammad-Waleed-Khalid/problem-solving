def longest_valid_parentheses(s):
    left = right = maxlength = 0
    for i in range(len(s)):
        if s[i] == '(':
            left += 1
        elif s[i] == ')':
            right += 1
        if left == right:
            maxlength = max(maxlength, 2*right)
        elif right>=left:
            left = right = 0
    left = right = 0
    for i in range(len(s)-1,0,-1):
        if s[i] == '(':
            left += 1
        elif s[i] == ')':
            right += 1
        if left == right:
            maxlength = max(maxlength, 2*left)
        elif left>=right:
            left = right = 0
    
    return maxlength

def main():
	input_str = ["(()", ")()())","", "(", ")()()(", ")())((())())("]
	for i in range(len(input_str)):
		result = longest_valid_parentheses(input_str[i])
		print(str(i+1) +".  longest_valid_parentheses(\"" + input_str[i] + "\"): " + str(result))
		print ("--------------------------------------------------------------------------------------\n")
if __name__ == "__main__":
	main()