class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashmap = {i : [] for i in range(numCourses)}
        hashset = set()


        for crs, pre in prerequisites:
            hashmap[crs].append(pre)
        
        def dfs(crs):
            if crs in hashset:
                return False
            if hashmap[crs] == []:
                return True
            
            hashset.add(crs)
            for pre in hashmap[crs]:
                if not dfs(pre): return False
            hashset.remove(crs)
            hashmap[crs] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False
        
        return True
            