word = input("Enter your Word:")

rev_word = word[::-1]

if word == rev_word:
	print("It is Palindrome")
else: 
	print("It is Not a Palindrome")
