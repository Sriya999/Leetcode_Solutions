class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt=0
        for digit in nums:
            if len(str(digit))%2==0:
                cnt+=1
        return cnt


        
