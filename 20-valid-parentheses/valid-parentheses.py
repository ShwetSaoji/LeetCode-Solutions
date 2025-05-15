class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')':'(',']':'[','}':'{'}

        stack = []

        for i in s:
            if i in '({[':
                stack.append(i)
            else:
                if not stack:
                    return False
                if stack.pop() != hashmap[i]:
                    return False
                continue
        
        if stack:
            return False
        else:
            return True