class Solution:
    def reverseWords(self, s: str) -> str:
        temp = s.split()
        temp.reverse()
        ans = " ".join(temp)

        return ans
