class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {')':'(', ']': '[', '}':'{'}
        stack = []

        for i in s:
            if i in '({[':
                stack.append(i)
            else:
                if stack: 
                    if stack.pop() != hmap[i]:
                        return False
                else:
                    stack.append(i)
        
        if stack:
            return False
        else:
            return True
