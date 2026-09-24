class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for i in tokens:
            # print(stack,i)

            if i == "+" or i == "-" or i == "*" or i == "/":
                y = stack.pop()
                x = stack.pop()

                stack.append(str(int(eval("".join([x,i,y])))))

            else:
                stack.append(i)
        # print(stack)
        return int(stack[-1])