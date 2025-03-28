class Solution {
    public static int avg(int arr[], int r, int l, int threshold, int k) {
        int sum = 0;
        int average = 0;
        for (int i = r; i <= l; i++) {
            sum = sum + arr[i];
        }
        average = sum / k;
        return average;
    }

    public int numOfSubarrays(int[] arr, int k, int threshold) {
        int count = 0;
        int l = 0;
        for (int r = 0; r < arr.length - k + 1; r++) {
            l = r + k - 1;
            int ans = avg(arr, r, l, threshold, k);
            if (ans >= threshold) {
                count++;
            }
        }
        return count;
    }
}
