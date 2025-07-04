class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False

        visit = set()
        nei = [ [] for _ in range(n)]

        for e1, e2 in edges:
            nei[e1].append(e2)
            nei[e2].append(e1)
        
        def dfs(node, prev):
            if node in visit:
                return False
            # if nei[node] == []:
            #     return True
            visit.add(node)
            for i in nei[node]:
                if i == prev:
                    continue
                else:
                    if not dfs(i, node): return False
            return True
            
        # if not dfs(0, -1): return False
        # if len(visit) == n: 
        #     return True
        # else:
        #     return False
        return dfs(0, -1) and len(visit) == n