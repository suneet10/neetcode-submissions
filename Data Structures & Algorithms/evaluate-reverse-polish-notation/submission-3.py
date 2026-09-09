class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for i in tokens:
            # print(stack,i)

            if i == "+" or i == "-" or i == "*" or i == "/":
                y = stack.pop()
                x = stack.pop()

                if i == "+":
                    stack.append(x + y)
                elif i == "-":
                    stack.append(x - y)
                elif i == "*":
                    stack.append(x * y)
                elif i == "/":
                    stack.append(int(x / y))

            else:
                stack.append(int(i))
        # print(stack)
        return int(stack[-1])