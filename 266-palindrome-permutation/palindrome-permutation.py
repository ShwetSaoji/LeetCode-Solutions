class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        pair = set()

        for i in s:
            if i in pair:
                pair.remove(i)
            else:
                pair.add(i)
        
        return len(pair) <= 1