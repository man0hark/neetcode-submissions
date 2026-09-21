class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        rows, cols = len(grid), len(grid[0])
        res = 0
        def helper(r,c): 
            q = deque()
            grid[r][c] = "0"
            q.append((r,c))
            while q:
                row, col = q.popleft()
                for dr,dc in dirs:
                    xr,xc = row+dr, col+dc
                    if( xr<0 or xc <0 or xr >=rows or xc >=cols or grid[xr][xc]=="0"):
                        continue
                    q.append((xr,xc))
                    grid[xr][xc] = "0"  
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    helper(i,j)
                    res+=1

        return res