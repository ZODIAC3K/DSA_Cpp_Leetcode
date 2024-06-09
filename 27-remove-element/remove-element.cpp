class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        auto i = nums.begin();
        while(i != nums.end()){
            if(*i == val){
                i = nums.erase(i);  // Erase returns iterator to next element
            }else{
                ++i;  // Only increment the iterator if no erase occurred
            }
        }
        return nums.size();
    }
};