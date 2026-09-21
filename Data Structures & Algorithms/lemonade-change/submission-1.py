class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        i,j = 0,0
        for x in bills:
            if x==5:
                i+=1
            elif x==10:
                i,j = i-1, j+1
            elif j > 0:
                i,j = i-1, j-1
            else:
                i-=3
            if i<0:
                return False
        return True