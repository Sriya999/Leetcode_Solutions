class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1 #T.C:O(LOgN)
        m = n #negative numbers
        n = abs(n)
        while n > 0:
            if n % 2 == 1:
                ans = ans * x
                n = n - 1
            else:
                n = n // 2
                x = x * x

        return 1 / ans if m < 0 else ans
