class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int[] ans = new int[nums.length];
        int curr = 0;

        for(int i=0; i < nums.length; i++){
            for(int j=0;j<nums.length; j++){
                if(i == j){
                    continue;
                }
                else if(nums[j] < nums[i]){
                    curr++;
                }
            }
            ans[i] = curr;
            curr = 0;
        }

        return ans;
    }
}