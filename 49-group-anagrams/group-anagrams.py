class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}

        for i in strs:
            si = str(sorted(i))
            if si in hashMap:
                hashMap[si].append(i)
            else:
                hashMap[si] = [i]
        
        return list(hashMap.values())