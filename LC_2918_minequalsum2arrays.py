class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        zerocnt1=nums1.count(0)
        zerocnt2=nums2.count(0)
        sum1=sum(nums1)+zerocnt1
        sum2=sum(nums2)+zerocnt2
        if sum1==sum2:
            return sum1
        elif sum1>sum2:
            if zerocnt2>0:
                return sum1
        elif sum2>sum1:
            if zerocnt1>0:
                return sum2
        return -1

        
