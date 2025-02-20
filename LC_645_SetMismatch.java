class Solution {
    public int[] findErrorNums(int[] nums) {
        HashSet<Integer> s1 = new HashSet<>();

        int duplicate = -1;
        for (int i = 0; i < nums.length; i++) {
            if (!s1.contains(nums[i])) {
                s1.add(nums[i]);
            } else {
                duplicate = nums[i];// duplicate number

            }
        }
        // missing number
        int missed = -1;
        for (int i = 1; i <= nums.length; i++) {
            if (!s1.contains(i)) {
                missed = i;
                break;
            }
        }
        int res[] = { duplicate, missed };
        return res;
    }
}
