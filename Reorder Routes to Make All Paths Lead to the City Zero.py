class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.n = n
        self.connections = connections
        self.nei = {city : [] for city in range(self.n)}
        for a,b in self.connections:
            self.nei[a].append(b)
            self.nei[b].append(a)
        self.edges = {(a, b) for a, b in self.connections}
        self.visited = [0] * self.n
        self.visited[0] = 1
        self.ans = 0
        self.dfs(0)
        return self.ans

    def dfs(self, city):
        for nbr in self.nei[city]:
            if self.visited[nbr] == 1:
                continue
            if (nbr, city) not in self.edges:
                self.ans += 1
            self.visited[nbr] = 1
            self.dfs(nbr)
    
        
        
