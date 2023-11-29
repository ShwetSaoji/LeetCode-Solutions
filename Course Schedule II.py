class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        #Creating a graph with courses as parent, and prerequi courses as children
        pre = defaultdict(list)

        for course,prereq in prerequisites:
            pre[course].append(prereq)
        
        #Inititalizing the res as a list, this will store our final answer.
        result = []

        #creating empty sets 
        #set 1 - visited is for tracking visited nodes.
        visited = set()
        #set 2 - cycle is to track if the course is in a cyclic traversal
        cycle = set()

        #defining DFS Function, which would be called recursively 
        def dfs(num):
            # base case to check if the course is cyclic in graph
            if num in cycle:
                return False
            # base case to check if the course has already been visited
            if num in visited:
                return True
            #add the course to our current cycle
            cycle.add(num)
            for prereq in pre[num]:
                if dfs(prereq) == False:
                    return False
            cycle.remove(num)
            visited.add(num)
            result.append(num)
            return True

        for num in range(numCourses):
            if dfs(num) == False:
                return []
            
        return result
