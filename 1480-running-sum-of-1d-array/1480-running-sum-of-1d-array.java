class Solution {
    public int[] runningSum(int[] nums) {
        int[] ans = new int[nums.length];
        int sum = 0;

        for(int i=0; i<nums.length; i++){
            for(int j=0; j<i+1; j++){
                sum += nums[j];
            }
            ans[i] = sum;
            sum = 0;
        }

        return ans;
    }
}