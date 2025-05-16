class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i not in "+-*/":
                stack.append(i)
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if i == "+":
                    stack.append(a + b)
                elif i == "-":
                    stack.append(a-b)
                elif i == "*":
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))
            
        
        return int(stack.pop())
        # print(int((6)/-132))