class Solution:
    def longestPalindrome(self, s: str) -> int:
        hm = defaultdict(int)

        for i in s:
            hm[i] += 1

        hm = dict(sorted(hm.items(), key=lambda i:i[1], reverse=True))

        ans = 0 
        odd = True
        print(hm)
        for item, value in hm.items():
            if value%2 == 0:
                ans += value
            elif odd:
                ans += value
                odd = False
            else:
                ans = ans + value -1
        
        return ans
        