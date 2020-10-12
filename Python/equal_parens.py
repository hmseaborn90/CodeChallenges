# def validParenthesesSequence(str):
#     if len(str) % 2 is not 0:
#         return False
#     stack = []
#     for i in range(len(str)):
#         par = str[i]
#         if par == "(":
#             stack.append(par)
#         if par == ")" and len(stack):
#             stack.remove(stack[0])
#     if stack == []:
#         return True  
#     else:
#         return False 

def validParenthesesSequence(string):
    depth = 0
    
    for character in string:
        if character == "(":
            depth += 1
        elif character == ")":
            depth -= 1
            if depth == -1:
                return False
    
    return depth == 0