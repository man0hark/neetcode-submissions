/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    List<Integer> x = new ArrayList<>();
    public List<Integer> rightSideView(TreeNode root) {
        adder(root,0);
        return x;
        
    }
    public void adder(TreeNode node, int level)
    {
        if(node == null)
        {
            return;
        }

        if(x.size() == level)
        {
            x.add(node.val);
        }
        adder(node.right, level+1);
        adder(node.left,level+1);
    }
}
