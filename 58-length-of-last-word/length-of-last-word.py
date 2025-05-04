class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = 0 

        for i in range(len(s)-1, -1, -1):
            if s[i] == " " and ans == 0:
                continue
            else:
                if s[i] == " ":
                    break
                else:
                    ans += 1
        return ans