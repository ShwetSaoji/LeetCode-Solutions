class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_count = senate.count('R')
        d_count = senate.count('D')

        q = deque(senate)

        d_bancheck = 0
        r_bancheck = 0

        while r_count and d_count:
            curr = q.popleft()

            if curr == 'D':
                if d_bancheck:
                    d_bancheck -= 1
                    d_count -= 1
                else:
                    r_bancheck += 1
                    q.append(curr)
            else:
                if r_bancheck:
                    r_bancheck -= 1
                    r_count -= 1
                else:
                    d_bancheck += 1
                    q.append(curr)
        
        if r_count:
            return 'Radiant'
        else:
            return 'Dire'
