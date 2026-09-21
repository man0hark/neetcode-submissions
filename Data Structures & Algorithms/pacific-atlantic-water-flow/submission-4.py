class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def helper(node, ocean):
            q=deque(node)
            while q:
                r,c = q.popleft()
                ocean[r][c] = True
                for dr,dc in dirs:
                    nr,nc = r+dr, c+dc
                    if(0<=nr<rows and 0<=nc<cols and not ocean[nr][nc] and heights[nr][nc]>=heights[r][c]):
                        q.append((nr,nc))
        rows, cols = len(heights), len(heights[0])
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        pac = [[False]* cols for _ in range(rows)]
        atl = [[False]* cols for _ in range(rows)]

        paci, atli = [], []
        for i in range(rows):
            paci.append((i,0))
            atli.append((i, cols-1))
        for i in range(cols):
            paci.append((0,i))
            atli.append((rows-1,i))
        
        helper(paci,pac)
        helper(atli,atl)
        res=[]
        for i in range(rows):
            for j in range(cols):
                if pac[i][j] and atl[i][j]:
                    res.append([i,j])
        return res
