class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hashmap = {i:[] for i in range(numCourses)}
        hashset = set()
        visit = set()
        order = []

        for crs, pre in prerequisites:
            hashmap[crs].append(pre)
        
        def dfs(crs):
            if crs in hashset:
                return False
            if crs in visit:
                return True
            hashset.add(crs)
            for pre in hashmap[crs]:
                if not dfs(pre):
                    return False
            hashset.remove(crs)
            visit.add(crs)
            order.append(crs)
            hashmap[crs] = []
            return True



        for i in range(numCourses):
            if not dfs(i):
                return []
        return order