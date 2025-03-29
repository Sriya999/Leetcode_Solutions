class Solution {
    public int numOfSubarrays(int[] arr, int k, int threshold) {
        int res = 0, l = 0, temp = 0;
        for (int r = 0; r < arr.length; r++) {
            temp = temp + arr[r];
            if (r - l == k) {
  //subarray window size exceeds
                temp = temp - arr[l];
                l++;
            }
            if (r - l + 1 == k) { 
                int avg = temp / k;
                if (avg >= threshold) {
                    res++;
                }
            }
        }
        return res;
    }
}
