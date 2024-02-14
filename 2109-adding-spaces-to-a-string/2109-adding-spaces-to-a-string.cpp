class Solution {
public:
    string addSpaces(string s, vector<int>& spaces) {
        string newStr = "";
        int tracker = 0;
        for(int i=0; i<s.length(); i++){
            if(tracker < spaces.size() && i == spaces[tracker]){
                newStr+= " ";
                newStr+= s[i];
                tracker++;
            }
            else{
                newStr+= s[i];
            }
        }

        return newStr;
    }
};