class Solution {
    public int mostWordsFound(String[] sentences) {
        int maxwords = 0;
        for (int i = 0; i < sentences.length; i++) {
            String s = sentences[i];
            String wordslist[] = s.split("\\s");
            maxwords = Math.max(maxwords, wordslist.length);

        }
        return maxwords;
    }
}