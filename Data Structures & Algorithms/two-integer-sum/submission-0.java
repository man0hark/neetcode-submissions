class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> n = new HashMap<>();
        for(int i=0; i<nums.length; i++)
        {
            int d = target - nums[i];
            if(n.containsKey(d)) return new int[]{n.get(d),i};
            n.put(nums[i], i);
        }
        return new int[]{};
    }
}
