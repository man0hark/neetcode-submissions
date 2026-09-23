class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1

        while l<r:
            while not self.alphanum(s[l]) and l<r:
                l+=1
            while not self.alphanum(s[r]) and r>l:
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l,r = l+1, r-1
        return True

    def alphanum(self, i):
        return ord('A') <= ord(i) <= ord('Z') or ord('a') <= ord(i) <= ord('z') or ord('0')<= ord(i) <= ord('9')