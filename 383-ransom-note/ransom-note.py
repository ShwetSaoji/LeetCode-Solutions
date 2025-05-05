class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hm_r = defaultdict(int)
        hm_m = defaultdict(int)

        for i in ransomNote:
            hm_r[i] += 1
        
        for i in magazine:
            hm_m[i] += 1
        
        for item, value in hm_r.items():
            if hm_m[item] < value:
                return False
        
        return True