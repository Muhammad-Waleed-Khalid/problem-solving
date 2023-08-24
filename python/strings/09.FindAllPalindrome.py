import json
def getPalindromes(input_string,palindromes,j,k):
	while j >= 0 and k < len(input_string):
		if input_string[j] != input_string[k]:
			break
		palindromes.append(input_string[j: k+1])
		j -= 1
		k += 1

def find_all_palindrome_substrings(input_string):
	pal = []
	for i in range(len(input_string)):
		getPalindromes(input_string,pal,i,i+1)
		getPalindromes(input_string,pal,i-1,i+1)
	return pal


def main():
    input_string = ["aabbbaa", "321230990", "educative"]
    for i in range(len(input_string)):
        result = find_all_palindrome_substrings(input_string[i])
        print(str(i+1) + ". Input string: " + str(input_string[i]))
        print("   Palindromes: " + json.dumps(result))
        print("   Total palindrome substrings: ", len(result))
        print("-"*100)

if __name__ == '__main__':
    main()