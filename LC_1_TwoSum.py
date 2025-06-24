class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for i in range(0,len(nums)):
            diff=target-nums[i]
            if diff in map:#other pair already appeared in array return index
                return [map[diff],i]
            map[nums[i]]=i
            
        return []

        
