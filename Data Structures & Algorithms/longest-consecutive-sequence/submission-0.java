class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> x = new HashSet<>();
        int maxl=0;
        for(int i: nums)
        {
            x.add(i);
        }
        for(int j : x)
        {
            if(!x.contains(j-1))
            {
                int l = 1;
                while(x.contains(j+l))
                {
                    l++;
                }
                maxl = Math.max(l,maxl);
            }
        }
        return maxl;
    }
}
