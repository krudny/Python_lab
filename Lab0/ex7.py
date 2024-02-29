def val(expression):
    stack = []

    for char in expression:
        if char in '01':
            stack.append(char)
        else:
            p = int(stack.pop())
            q = int(stack.pop())

            if char == '|':
                stack.append(p or q)
            elif char == '&':
                stack.append(p and q)
            else:
                stack.append(p or 1 - q)

    return stack[0]

