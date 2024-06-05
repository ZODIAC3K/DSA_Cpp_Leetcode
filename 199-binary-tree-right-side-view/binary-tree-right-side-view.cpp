/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {

        vector<int>result;
        rightView(root, result, 0);
        return result;


    }
    void rightView(TreeNode* node, vector<int> &result, int level){
        if(node == NULL){
            return;
        }
        if(level == result.size()){
            result.push_back(node->val);
        }
        rightView(node->right, result, level+1);
        rightView(node->left, result, level+1);

    }
};