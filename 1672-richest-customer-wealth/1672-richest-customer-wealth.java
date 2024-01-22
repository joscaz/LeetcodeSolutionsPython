class Solution {
    public int maximumWealth(int[][] accounts) {
        int curr = 0, maximum = 0;
        
        for(int i=0; i<accounts.length; i++){
            for(int j=0; j<accounts[i].length; j++){
                curr += accounts[i][j];
            }
            
            maximum = Math.max(maximum, curr);
            curr = 0;
        }
        
        return maximum;
    }
}