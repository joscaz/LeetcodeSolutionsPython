class Solution {
    public int finalValueAfterOperations(String[] operations) {
        int initial = 0;

        for(String operation : operations){
            if(operation.contains("-")){
                initial--;
            }else{
                initial++;
            }
        }

        return initial;
    }
}