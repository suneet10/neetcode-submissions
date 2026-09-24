class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for i in tokens:

            if i == "+" or i == "-" or i == "*" or i == "/":
                y = stack.pop()
                x = stack.pop()

                stack.append(str(eval("".join([x,i,y]))))

            else:
                stack.append(i)

        return eval(stack[-1])