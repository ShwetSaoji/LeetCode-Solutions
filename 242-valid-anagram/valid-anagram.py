class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) : return False
        s_sort = sorted(s)
        t_sort = sorted(t)

        # for i in range(len(s_sort)):
        #     if s_sort[i] != t_sort[i]:
        #         return False
        
        # return True

        return s_sort == t_sort