package template;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class BinaryTree {
    // define tree node
    public class TreeNode {
        public int val;
        public TreeNode left, right;

        public TreeNode(int val) {
            this.val = val;
            this.left = this.right = null;
        }
    }

    /**
     * recursive traversal
     * @param root current node
     * @param result result list
     */
    private void recursiveTraverse(TreeNode root, ArrayList<Integer> result) {
        if (root == null) {
            return;
        }
        // preorder
        result.add(root.val);
        recursiveTraverse(root.left, result);
        // inorder
        // "result.add(root.val);"
        recursiveTraverse(root.right, result);
        // postorder
        // "result.add(root.val);"
    }
    
    /**
     * entry function
     * @param root root node
     * @return result list
     */
    public ArrayList<Integer> entry(TreeNode root) {
        ArrayList<Integer> result = new ArrayList<>();
        recursiveTraverse(root, result);
        return result;
    }


    /**
     * devide and conquer traversal
     * @param root root node
     * @return result list
     */
    public ArrayList<Integer> devideAndConquerTraverse(TreeNode root) {
        ArrayList<Integer> result = new ArrayList<>();
        if (root == null) {
            return result;
        }

        // devide
        ArrayList<Integer> left = devideAndConquerTraverse(root.left);
        ArrayList<Integer> right = devideAndConquerTraverse(root.right);

        // conquer
        // preorder
        result.add(root.val);
        result.addAll(left);
        // inorder
        // "result.add(root.val);"
        result.addAll(right);
        // postorder
        // "result.add(root.val);"
        return result;
    }

    public List<Integer> preorderTraversal(TreeNode root) {
        Stack<TreeNode> stack = new Stack<TreeNode>();
        List<Integer> preorder = new ArrayList<Integer>();
        
        if (root == null) {
            return preorder;
        }
        
        stack.push(root);
        while (!stack.empty()) {
            TreeNode node = stack.pop();
            preorder.add(node.val);
            if (node.right != null) {
                stack.push(node.right);
            }
            if (node.left != null) {
                stack.push(node.left);
            }
        }
        
        return preorder;
    }

    public ArrayList<Integer> inorderTraversal(TreeNode root) {
        Stack<TreeNode> stack = new Stack<>();
        ArrayList<Integer> result = new ArrayList<>();
        
        while (root != null) {
            stack.push(root);
            root = root.left;
        }
    
        while (!stack.isEmpty()) {
            TreeNode node = stack.peek();
            result.add(node.val);
            
            if (node.right == null) {
                node = stack.pop();
                while (!stack.isEmpty() && stack.peek().right == node) {
                    node = stack.pop();
                }
            } else {
                node = node.right;
                while (node != null) {
                    stack.push(node);
                    node = node.left;
                }
            }
        }
        return result;
    }

    public ArrayList<Integer> postorderTraversal(TreeNode root) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode prev = null; // previously traversed node
        TreeNode curr = root;
    
        if (root == null) {
            return result;
        }
    
        stack.push(root);
        while (!stack.empty()) {
            curr = stack.peek();
            if (prev == null || prev.left == curr || prev.right == curr) { // traverse down the tree
                if (curr.left != null) {
                    stack.push(curr.left);
                } else if (curr.right != null) {
                    stack.push(curr.right);
                }
            } else if (curr.left == prev) { // traverse up the tree from the left
                if (curr.right != null) {
                    stack.push(curr.right);
                }
            } else { // traverse up the tree from the right
                result.add(curr.val);
                stack.pop();
            }
            prev = curr;
        }
    
        return result;
    }

}
