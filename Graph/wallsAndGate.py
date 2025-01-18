from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def addDistance(r,c):
            if r not in range(rows) or c not in range(cols) or grid[r][c] == -1 or (r,c) in visited:
                return
            visited.add((r,c))
            queue.append((r,c))
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        visited = set()
        distance = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i,j))
        
        while queue:
            for element in range(len(queue)):
                element = queue.popleft()
                r,c = element[0],element[1]
                grid[r][c] = distance
                visited.add((r,c))   

                addDistance(r+1,c)
                addDistance(r-1,c)
                addDistance(r,c+1)
                addDistance(r,c-1)
            distance += 1
