class Solution:
    def removeStars(self, s: str) -> str:
        arr = []

        for i in range(len(s)):
            if s[i] != "*":
                arr.append(s[i])
            else:
                arr.pop()
        
        return "".join(arr)
