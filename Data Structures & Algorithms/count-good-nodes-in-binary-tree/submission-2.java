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
    public int goodNodes(TreeNode root) {
        return dfs(root, root.val);
    }
    private int dfs(TreeNode node, int maxval)
    {
        if(node==null)
        {
            return 0;
        }
        int x = (node.val >= maxval) ? 1:0;
        maxval = Math.max(maxval, node.val);
        x+=dfs(node.right,maxval);
        x+=dfs(node.left,maxval);
        return x;
    }
}
