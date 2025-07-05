class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        if n==0:
            return 0
        
        #compute left max
        prefixmax=[0]*n
        #firstelement leftmax is itself
        prefixmax[0]=height[0]
        for i in range(1,n):
            prefixmax[i]=max(prefixmax[i-1],height[i])
        
        #compute right max
        suffixmax=[0]*n
        #last element is max for itself
        suffixmax[n-1]=height[n-1]
        for i in range(n-2,-1,-1):
            suffixmax[i]=max(suffixmax[i+1],height[i])
        
        totalw=0
        for i in range(len(height)):
            if prefixmax[i]>height[i] and height[i]<suffixmax[i]:
                totalw+=min(prefixmax[i],suffixmax[i])-height[i]#take min height
        return totalw

        
