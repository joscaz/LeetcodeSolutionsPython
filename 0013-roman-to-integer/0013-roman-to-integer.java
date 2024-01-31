class Solution {
    public int romanToInt(String s) {
        int i = 0, ans = 0;
        Map<Character, Integer> romans = new HashMap<>();

        romans.put('I', 1);
        romans.put('V', 5);
        romans.put('X', 10);
        romans.put('L', 50);
        romans.put('C', 100);
        romans.put('D', 500);
        romans.put('M', 1000);

        while (i < s.length()){
            if(i == s.length() - 1){
                ans += romans.get(s.charAt(i));
                i++;
            }
            else if(romans.get(s.charAt(i)) < romans.get(s.charAt(i+1))){
                ans += romans.get(s.charAt(i + 1)) - romans.get(s.charAt(i));
                i+=2;
            }
            else{
                ans += romans.get(s.charAt(i));
                i++;
            }
            
        }

        return ans;

    }
}