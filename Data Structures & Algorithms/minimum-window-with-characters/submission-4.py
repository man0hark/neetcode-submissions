class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        count1, count2 = {}, {}
        for i in t:
            count1[i] = count1.get(i, 0) + 1
        
        have = 0
        target = len(count1)
        coordinates = [-1, -1]
        reslen = float("infinity")
        l = 0
        
        for r in range(len(s)):
            c = s[r]
            count2[c] = count2.get(c, 0) + 1

            if c in count1 and count1[c] == count2[c]:
                have += 1

            while have == target:
                if (r - l + 1) < reslen:
                    coordinates = [l, r]
                    reslen = r - l + 1
                
                count2[s[l]] -= 1
                if s[l] in count1 and count2[s[l]] < count1[s[l]]:
                    have -= 1
                l += 1

        l, r = coordinates
        return s[l:r+1] if reslen != float("infinity") else ""