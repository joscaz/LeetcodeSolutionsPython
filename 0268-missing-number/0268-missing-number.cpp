class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int cur_idx = 0;

        sort(nums.begin(), nums.end());

        for(int i = 0; i < n; i++){
            if(cur_idx != nums[i]){
                return cur_idx;
            }

            cur_idx++;
        }

        return cur_idx;

    }
};