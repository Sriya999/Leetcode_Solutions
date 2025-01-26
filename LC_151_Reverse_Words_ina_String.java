class Solution {
    public String reverseWords(String s) {
        s = s.trim();
     
        String ans = "";
        int n = s.length();
        StringBuilder res = new StringBuilder(s);
        res=res.reverse();
        for (int i = 0; i < n; i++) {
            String word = "";
            while (i < n && res.charAt(i) != ' ') {//identifying each words
                word = word + res.charAt(i);
                i++;
            }
            StringBuilder revword = new StringBuilder(word);
            revword = revword.reverse();//reversing each word
            if (word.length() > 0) {
                ans = ans + revword.toString() + " ";//result with extra space at end
            }
        }
        return ans.trim();
    }
}