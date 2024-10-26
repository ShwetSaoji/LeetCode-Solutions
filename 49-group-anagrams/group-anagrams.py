class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashset = defaultdict(list)

        # for i in strs:
        #     sort_str = ''.join(sorted(i))
        #     if sort_str in hashset:
        #         hashset[sort_str].append(i)
        #     else:
        #         hashset[sort_str] = [i]

        for s in strs:
            chars = [0] * 26
            for c in s:
                chars[ord(c) - ord("a")] += 1

            hashset[tuple(chars)].append(s)    

        return list(hashset.values())