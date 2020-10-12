    stack = []
    if sequence == "" or sequence == None:
        return None
    elif len(sequence) % 2 != 0:
        return False
    else:
        for x in sequence:
            if x == "{":
                stack.append("{")
            elif x == "}" and stack[-1] == "{":
                stack.pop()
            elif x == "[":
                stack.append("[")
            elif x == "]" and stack[-1] == "[":
                stack.pop()
            elif x == "(":
                stack.append("(")
            elif x == ")" and stack[-1] == "(":
                stack.pop()

        if len(stack) == 0:
            return True
        else:
            return False