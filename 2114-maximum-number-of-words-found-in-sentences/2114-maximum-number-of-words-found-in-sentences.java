class Solution {
    public int mostWordsFound(String[] sentences) {
        int max_words = 0, curr_words = 0;
        for (String sentence : sentences){
            for(int i=0; i<sentence.length(); i++){
                if(sentence.charAt(i) == ' '){
                    curr_words++;
                }
            }

            curr_words++;
            max_words = Math.max(max_words, curr_words);
            curr_words = 0;
        }

        return max_words;
    }
}