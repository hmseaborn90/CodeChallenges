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




def delDupunsorted(self):
temp=self.head
while temp != None:
temp2=temp

print(temp.data , temp2.next.data)
while temp2.next != None:
if temp.data == temp2.next.data:
dup=temp2.next
temp2.next=temp2.next.next
print("if")
del dup
else:
temp2=temp2.next
print("else")

temp=temp.next