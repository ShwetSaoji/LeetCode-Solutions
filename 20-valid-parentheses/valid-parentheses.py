class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {'}':'{', ']':'[', ')':'('}

        stack = []

        for i in s:
            if i in '{([':
                stack.append(i)
            else:
                if not stack or stack.pop() != hashmap[i]:
                    return False
            
        
        if stack:
            return False
        else:
            return True
        