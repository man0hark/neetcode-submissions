class Solution {
    public int maxArea(int[] heights) {
        int i = 0;
        int j = heights.length-1;
        int maxc = 0;
        while(i<j)
        {
            int temp=(j-i)*Math.min(heights[i], heights[j]);
            maxc = Math.max(maxc, temp);
            if(heights[i] <= heights[j])
            {
                i++;
            }
            else
            {
                j--;
            }
        }
        return maxc;
    }
}
