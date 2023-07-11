def isPalindrome(s):
	# Convert the string to lowercase and remove non-alphanumeric characters
	cleaned_string = ''.join(char.lower() for char in s if char.isalnum())

	# Check if the cleaned string is equal to its reverse
	return cleaned_string == cleaned_string[::-1]


print(isPalindrome("A man, a plan, a canal: Panama"))  # True
print(isPalindrome("race a car"))  # False
