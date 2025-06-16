class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg_cnt=self.binarysearch(nums,0)
        pos_cnt=len(nums)-self.binarysearch(nums,1)
        return max(neg_cnt,pos_cnt)
        
    def binarysearch(self,nums,t):
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==t:
                r=mid-1
            elif nums[mid]<t:
                l=mid+1
            else:
                r=mid-1
        return l

        
