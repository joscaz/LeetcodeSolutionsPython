class Solution {
public:
    int firstUniqChar(string s) {
        unordered_map<string, int> hm;

        for(char ch : s){
            string key(1, ch);
            if(hm.find(key) == hm.end()){
                hm[key] = 0;
            }
            hm[key]++;
        }

        for(int i=0; i < s.length(); i++){
            string key(1, s[i]);
            if(hm[key] == 1){
                return i;
            }
        }

        return -1;
    }
};