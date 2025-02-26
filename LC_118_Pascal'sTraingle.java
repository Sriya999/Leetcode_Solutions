class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> ans = new ArrayList<>();
        // usually first elem is [1]
        ArrayList<Integer> firstrow = new ArrayList<>();
        firstrow.add(1);
        // insert first ele
        ans.add(firstrow);
        for (int i = 1; i < numRows; i++) {
            ArrayList<Integer> temp = new ArrayList<>();
            temp.add(1);
            for (int j = 1; j < i; j++) {
                int val = ans.get(i - 1).get(j) + ans.get(i - 1).get(j - 1);
                temp.add(val);
            }

            temp.add(1);
            ans.add(temp);
        }

        return ans;
    }
}
