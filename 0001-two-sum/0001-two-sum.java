class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> hm = new HashMap<>();
        int diff;
        
        for(int i=0; i<nums.length; i++){
            diff = target - nums[i];
            
            if (hm.containsKey(diff)){
                return new int[]{i, hm.get(diff)};
            }
            
            hm.put(nums[i], i);
        }
        
        return null;
    }
}