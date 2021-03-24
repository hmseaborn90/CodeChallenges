def valid_parentheses(string):
#     if len(string) % 2 is not 0:
#         return False
    #your code here
    #create a list to act as our stack    
    stack = []
    #loop through our string 
    for character in string:
    
    #if "(" append to our stack
        if character == "(":
            stack.append(character)
    #else if ")" and our stack has length remove first opening bracket 
        elif character == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
            
    # compare stack to []

    return stack == []