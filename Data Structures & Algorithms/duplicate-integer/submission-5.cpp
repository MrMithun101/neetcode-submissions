class Solution {
public:

    std::vector<int> seen = {};

    bool hasDuplicate(vector<int>& nums) {
        for(int i = 0; i < nums.size(); i++){
            for(int j = 0; j < seen.size(); j++){
                if(nums[i] == seen[j]){
                    return true;
                }

            }
            seen.push_back(nums[i]);
        }
        return false;

    }
    
};