class Solution {
    public boolean isIsomorphic(String s, String t) {
        HashMap<Character, Character> map = new HashMap<>();
        HashMap<Character, Character> rev = new HashMap<>();
        //if not same length not isometric strings
        if (s.length() != t.length()) {
            return false;
        }
        boolean ans = true;
        for (int i = 0; i < s.length(); i++) {
            char sch = s.charAt(i);
            char tch = t.charAt(i);
            if (!map.containsKey(sch) && !rev.containsKey(tch)) {
                map.put(sch, tch);
                rev.put(tch, sch);
            } else if (map.containsKey(sch) && map.get(sch) != tch) {
                ans = false;
                break;
            } else if (rev.containsKey(tch) && rev.get(tch) != sch) {
                ans = false;
                break;
            }
        }

        return ans;
    }
}
