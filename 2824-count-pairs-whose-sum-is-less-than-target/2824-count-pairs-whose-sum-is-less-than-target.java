class Solution {
    public int countPairs(List<Integer> nums, int target) {
        // i >= 0
        // i < j 
        // j < n
        // n = length

        int count = 0;

        for(int i=0; i < nums.size(); i++){
            for(int j=0; j<nums.size(); j++){
                if(i < j && (nums.get(i) + nums.get(j)) < target){
                    count++;
                }
            }
        }

        return count;
    }
}