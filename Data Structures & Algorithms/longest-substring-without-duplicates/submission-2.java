class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> x = new HashSet<>();
        int l = 0;
        int result = 0;
        for(int r = 0; r<s.length();r++)
        {
            while(x.contains(s.charAt(r)))
            {
                x.remove(s.charAt(l));
                l++;
            }
            x.add(s.charAt(r));
            result = Math.max(r-l+1, result);
        }
        return result;
    }
}
