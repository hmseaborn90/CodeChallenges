def fizz_buzz(num):
	output = ""
	if num % 3 == 0:
		output += "Fizz"
		return output
	if num % 5 == 0:
		output += "Buzz"
		return output
	return str(num)	