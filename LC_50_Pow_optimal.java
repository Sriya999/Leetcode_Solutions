class Solution {
    public double myPow(double x, int n) {
        double ans = 1;
        long abs_n = Math.abs((long)n);// make positive
        
        while (abs_n > 0) {
            if (abs_n % 2 == 1) {
                ans = ans * x;
                abs_n = abs_n - 1;
            } else {
                x = x * x;
                abs_n =abs_n/2;
            }
        }
        if (n < 0) {
            return 1 / ans;
        } else {
            return ans;
        }
    }
}
