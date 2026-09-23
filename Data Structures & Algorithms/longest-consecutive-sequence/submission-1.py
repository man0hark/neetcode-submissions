class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        longest = 0
        for i in nset:
            if i-1 not in nset:
                l = 1
                while i+l in nset:
                    l+=1
                longest = max(l,longest)
        return longest