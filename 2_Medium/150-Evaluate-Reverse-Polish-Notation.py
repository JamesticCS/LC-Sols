class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(['+', '-', '*', '/'])
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                if token == '+':
                    x = stack.pop()
                    y = stack.pop()
                    stack.append(x+y)
                elif token == '-':
                    x = stack.pop()
                    y = stack.pop()
                    stack.append(y-x) 
                elif token == '/':
                    x = stack.pop()
                    y = stack.pop()
                    stack.append(int(y/x))                 
                elif token == '*':
                    x = stack.pop()
                    y = stack.pop()
                    stack.append(x*y) 

        return stack[0]
