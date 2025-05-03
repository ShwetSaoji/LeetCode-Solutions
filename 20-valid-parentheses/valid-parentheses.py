class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hm = {'}':'{', ']':'[',')':'('}

        for i in s:
            if i in '([{':
                stack.append(i)
            else:
                if stack:
                    if stack.pop() != hm[i]:
                        return False
                else:
                    return False
        
        if stack:
            return False
        else:
            return True