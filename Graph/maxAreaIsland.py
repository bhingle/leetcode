class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0
        def dfs(r,c, count):
            if grid[r][c] == 0:
                return 0
            visited.add((r,c))
            count += 1

            directions = [[-1,0],[1,0],[0,1],[0,-1]]
            for direction in directions:
                new_row = direction[0]
                new_col = direction[1]
                new_row += r
                new_col += c
                
                if new_row in range(rows) and new_col in range(cols) and (new_row,new_col) not in visited and grid[new_row][new_col] == 1:
                    count = dfs(new_row,new_col,count)
            return count
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == 1:
                    maxArea = max(maxArea,dfs(r,c,0))
        return maxArea