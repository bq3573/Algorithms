"""
	Brandon Quinn

"""

# function is palindrome attached to a strong...


def palindrome_subdivisions(word):
	# count = 0
	# Base case should be no chars
	if len(word) == 0:
		return 1

	count = 0
	for x in range(len(word)):
		if is_palindrome(word[x:]):
			count += palindrome_subdivisions(word[:x])

	return count


def is_palindrome(word):
	return True if word == word[::-1] else False


def main():
	# line = "abc"
	# print(palindrome_subdivisions(line))
	n = int(input())
	lines = [input() for _ in range(n)]
	for line in lines:
		print(palindrome_subdivisions(line))
	# palindrome_subdivisions("abc")


if __name__ == "__main__":
	main()
