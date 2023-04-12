class Solution:
    def isValid(self, s: str) -> bool:
        #let create empty stack; return true if its empty and false if its not.
        stack = []

        #let create a hashmap to map/pair the opening and closing brackets.
        closetoopenbrackets = {")":"(", "]":'[', "}":"{"}

        for i in s:
            #to check if i is closing bracket or opening bracket.
            #if i is closing bracket
            if i in closetoopenbrackets: #if the i is present as a key in dic
                if stack and stack[-1] == closetoopenbrackets[i]:
                    stack.pop()
                else:
                    return False
            #if key/i open bracket, append stack        
            else:
                stack.append(i)
        
        return True if not stack else False
