class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count1,count2 = [0]*26, [0]*26

        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')]+=1

        for i in range(len(s2) - len(s1) + 1):
            count2 = [0]*26
            for k in s2[i:i + len(s1)]:
                count2[ord(k) - ord('a')]+=1
            if count1 == count2:
                return True

        return False