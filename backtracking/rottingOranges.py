from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append([i,j])
                elif grid[i][j] == 1:
                    fresh += 1
        

        
        minutes = 0
        while queue and fresh > 0:
            currentLength = len(queue)
            directions = [[-1,0],[1,0],[0,1],[0,-1]]
            for i in range(currentLength):
                r,c = queue.popleft()
                for d in directions:
                    newRow = r + d[0]
                    newCol = c + d[1]

                    if newRow not in range(rows) or newCol not in range(cols) or grid[newRow][newCol] == 0 or grid[newRow][newCol] == 2:
                        continue
                    
                    queue.append((newRow,newCol))
                    grid[newRow][newCol] = 2
                    fresh -= 1

            minutes += 1
        if fresh ==0:
            return minutes
        return -1
        
        