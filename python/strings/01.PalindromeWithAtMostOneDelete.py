def check_palindrome(s):
    i = 0 
    n = len(s)-1
    while i < n:
        if s[i] != s[n]:
            return False
        i += 1
        n -= 1
    return True

def check_palindrome_with_1_delete(s):
    i = 0 
    n = len(s)-1
    while i < n:
        if s[i] != s[n]:
            return check_palindrome(s[i+1:n+1]) or check_palindrome(s[i:n])
        i += 1
        n -= 1
    return True

print("Yes Palindrome" if check_palindrome_with_1_delete("abca") else "Not a palindrome" )
print("Yes Palindrome" if check_palindrome_with_1_delete("abba") else "Not a palindrome" )
print("Yes Palindrome" if check_palindrome_with_1_delete("abcc") else "Not a palindrome" )