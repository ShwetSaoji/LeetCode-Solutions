class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        chars = set()

        for i in s:
            if i in chars:
                chars.remove(i)
            else:
                chars.add(i)

        return len(chars) <= 1


        