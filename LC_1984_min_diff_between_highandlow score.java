class Solution {
    public int minimumDifference(int[] nums, int k) {
        Arrays.sort(nums);
        int l = 0;
        int ans = Integer.MAX_VALUE;
        for (int r = 0; r < nums.length - k + 1; r++) {
            int j = r + k - 1;
            int temp = nums[j] - nums[r];
            ans = Math.min(temp, ans);
        }
        return ans;
    }
}
