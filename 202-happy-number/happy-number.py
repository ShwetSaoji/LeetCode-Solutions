class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n not in seen and n != 1:
            tot=0
            seen.add(n)
            n = str(n)
            for i in range(len(n)):
                tot+=int(n[i]) ** 2
            n = tot
        
        if n==1:
            return True
        else:
            return False