class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0 
        
        stack = []
        currnum = 0 
        currop = '+'
        
        for i, char in enumerate(s):
            if char.isdigit():
                currnum = currnum * 10 + int(char)
            if (not char.isdigit() and not char.isspace()) or i == len(s) - 1:
                if currop == '+':
                    stack.append(currnum)
                elif currop == '-':
                    stack.append(-currnum)
                elif currop == '*':
                    stack.append(stack.pop() * currnum)
                elif currop == '/':
                    top = stack.pop()
                    stack.append( int(top / currnum))
                currop = char
                currnum = 0 
        
        return sum(stack)