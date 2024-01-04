class Solution {
    public boolean isPalindrome(int x) {
        String strx = Integer.toString(x);
        int i = 0;
        int j = strx.length() - 1;

        while(i<=j){
            if(strx.charAt(i) == strx.charAt(j)){
                i++;
                j--;
            }
            else{
                return false;
            }
        }
        return true;
    }
}