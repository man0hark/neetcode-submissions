class Solution:
    def countBits(self, n: int) -> List[int]:
        '''
        res = []
        res.append(0)
        for i in range(1,n+1):
            count=0
            while i>0:
                count+=i&1
                i>>=1
            res.append(count)
        return res
        '''
        dp = [0] *(n+1)
        for i in range(n+1):
            dp[i] = (i&1) + dp[i>>1]
        return dp