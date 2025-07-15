class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - len(edges) != 1:
            return False
        
        visit = set()

        hashmap = {i:[] for i in range(n)}

        for node, nei in edges:
            hashmap[node].append(nei)
            hashmap[nei].append(node)

        def dfs(node, prev):
            if node in visit:
                return False
            visit.add(node)
            for nei in hashmap[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            return True
                
        if not dfs(0, -1):
            return False
        return len(visit) == n