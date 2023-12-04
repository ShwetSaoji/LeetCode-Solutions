class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        x_coor = defaultdict(list)
        y_coor = defaultdict(list)

        #Creating a copy of our input points in the form of tuples.
        copy = {(a,b) for a,b in stones}
        #initializing the number of distinct connected groups to 0
        grp = 0

        #creating graphs to maintain all x and y nodes of our input.
        for a, b in stones:
            x_coor[a].append(b)
            y_coor[b].append(a)

        #defining our depth first search logic to traverse through our input.
        def DFS(a,b):
            #since we are visitng the points (a,b) , remove it from our copy.
            copy.discard((a,b))
            #checking all y coor with our 0th value of input
            for y in x_coor[a]:
                if (a,y) in copy:
                    #recursive call until all the points are removed from copy.
                    DFS(a,y)
            #checking all x coor with our 1st value of input
            for x in y_coor[b]:
                if (x,b) in copy:
                    #recursive call until all the points are removed from copy.
                    DFS(x,b)

        #Calling our DFS function for every point of our input,  which would recursively call itself 
        for a, b in stones:
            if (a,b) in copy:
                DFS(a,b)
                grp += 1
        
        #Once our DFS traverses through all the points, we would have the number of distinct connected groups.
        #Our answer would be length of our input minus the distict groups, as we would need atleast one stone remaining to get a valid ans.
        return len(stones) - grp

        
