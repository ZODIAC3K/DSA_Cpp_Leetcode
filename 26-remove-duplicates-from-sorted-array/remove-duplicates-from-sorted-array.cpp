class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int j = 1; // because 1st element (nums[0]) is always unique so we start checking from next
        for(int i = 1; i < nums.size(); i++){
            if(nums[i] != nums[i - 1]){ // checks if prev element is same if not swap.
                nums[j] = nums[i];
                j++;
            }
        }
        return j;
    }
};