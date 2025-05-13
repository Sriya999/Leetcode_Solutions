class Solution:
    def maxArea(self, height: List[int]) -> int:
        area=0
        max_area=0
        for i in range(0,len(height)):
            for j in range(i+1,len(height)):
                width=j-i
                min_height=min(height[i],height[j])
                area=min_height*width
                max_area=max(max_area,area)
        return max_area
        
