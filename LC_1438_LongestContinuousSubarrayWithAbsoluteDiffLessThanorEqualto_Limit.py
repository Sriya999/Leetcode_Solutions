class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        longestlength=0
        mindq=deque()
        maxdq=deque()
        l=0
        for i in range(len(nums)):

            #store min of subarray in mindq
            while mindq and nums[mindq[-1]]>nums[i]:
                mindq.pop()
            mindq.append(i)

            #store max in subarray in maxdq
            while maxdq and nums[maxdq[-1]]<nums[i]:
                maxdq.pop()
            maxdq.append(i)

            #if diff exceeds limit shrink the window size
            while nums[maxdq[0]]-nums[mindq[0]]>limit:
                if mindq[0]==l:
                    mindq.popleft()
                if maxdq[0]==l:
                    maxdq.popleft()
                l+=1
            longestlength=max(i-l+1,longestlength)
        return longestlength
        


        
