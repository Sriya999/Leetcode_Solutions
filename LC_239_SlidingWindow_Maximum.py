class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq=deque()
        res=[]
        for i in range(len(nums)):
            #keep track of window tonot exceed window
            while dq and dq[0]<=i-k:
                dq.popleft()
            #remove less elements to store maximum curr element
            while dq and nums[dq[-1]]<nums[i]:
                dq.pop()
            #store curr max
            dq.append(i)
            #store res
            if dq and i>=k-1:
                res.append(nums[dq[0]])
        return res



        
        
