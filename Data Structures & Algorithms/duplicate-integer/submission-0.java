class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> x = new HashSet<>();
            for(int i : nums)
            {
                if(x.contains(i))
                {
                    return true;
                }
                x.add(i);
            }
            return false;
    }
}