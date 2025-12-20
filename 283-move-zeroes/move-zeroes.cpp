class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int insert = 0;

        for (int x : nums) {
            if (x != 0) {
                nums[insert++] = x;
            }
        }

        while (insert < nums.size()) {
            nums[insert++] = 0;
        }
    }
};