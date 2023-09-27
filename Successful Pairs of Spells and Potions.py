class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        mx = potions[-1]

        ans = []

        for i in spells:
            comp = (success + i - 1) // i
            print("comp is " + str(comp))

            if comp > mx:
                ans.append(0)
                continue
            index = bisect.bisect_left(potions, comp)
            print(index)
            ans.append(len(potions) - index)
        
            
        return ans
