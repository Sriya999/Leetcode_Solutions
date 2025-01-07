class Solution {
    public int numIdenticalPairs(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int countpairs = 0;//TC: O(N)
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(nums[i])) {
                countpairs = countpairs + map.get(nums[i]);
                // update frequency count Value in hash map
                map.put(nums[i], map.get(nums[i]) + 1);

            } else {
                map.put(nums[i], 1);
            }

        }
        return countpairs;
    }
}