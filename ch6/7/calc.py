def calc(expression):
    stack = []
    for c in expression.split(' '):
        print(stack)
        if c in {'+', '-', '*', '/'}:
            b, a = stack.pop(), stack.pop()
        else:
            stack.append(int(c))

        if c == '+':
            stack.append(a + b)
        elif c == '-':
            stack.append(a - b)
        elif c == '*':
            stack.append(a * b)
        elif c == '/':
            stack.append(a // b)

    return stack[0]

print(calc('4 6 2 + * 3 1 - 5 * -'))

