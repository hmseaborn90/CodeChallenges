def fizz_buzz(n):
    return_value = [ ]
    for c in range(1, n + 1):
        output = ""
        if c % 3 == 0:
            output += "Fizz"
        if c % 5 == 0:
            output += "Buzz"
        if output == "":
            output = str(c)
        return_value.append(output)
    return return_value
  
print(fizz_buzz(15))
