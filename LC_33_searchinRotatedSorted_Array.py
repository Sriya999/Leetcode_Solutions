class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #binary search
        l=0
        r=len(nums)-1
        while l<=r:
            mid=l+(r-l)//2
            if nums[mid]==target:
                return mid
            elif nums[l]<=nums[mid]:
                    #search in left sorted half
                    if nums[l]<=target and target<=nums[mid]:
                        r=mid-1
                    else:
                        #search in unsorted right half
                        l=mid+1
            else:
                #right half is sorted
                if nums[mid]<=nums[r]:
                    #check in right sorted half
                    if nums[mid]<=target and target<=nums[r]:
                        l=mid+1
                    else:
                        r=mid-1
        return -1


                
        
