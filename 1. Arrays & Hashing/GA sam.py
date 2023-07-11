s = 'Maybe we are togetha'
d = ''.join(char for char in s if char.isalnum())
print(d)



import timeit

# Initial function from the top of the chat
def isPalindrome(s):
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned_string == cleaned_string[::-1]

# Function we built at the end of the chat
def is_palindrome_without_spaces(s):
    d = ''.join(char for char in s if char != ' ')
    reversed_d = d[::-1]
    return d == reversed_d

# Testing execution time of both functions
s = "A man, a plan, a canal: Panama"

# Execution time for initial function
time_initial = timeit.timeit(lambda: isPalindrome(s), number=100000)

# Execution time for last function
time_last = timeit.timeit(lambda: is_palindrome_without_spaces(s), number=100000)

# Compare execution times and provide output
if time_initial < time_last:
    difference = time_last - time_initial
    fastest_function = "isPalindrome"
elif time_initial > time_last:
    difference = time_initial - time_last
    fastest_function = "is_palindrome_without_spaces"
else:
    difference = 0
    fastest_function = None

if fastest_function:
    print("Function", fastest_function, "is faster by:", difference)
else:
    print("Both functions have the same execution time.")
