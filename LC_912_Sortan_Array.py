class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(nums,low,high):
            if low>=high:#single element
                return
            mid=(low+high)//2
            mergeSort(nums,low,mid)
            mergeSort(nums,mid+1,high)
            merge(nums,low,mid,high)
        def merge(nums,low,mid,high):
            left=low
            right=mid+1
            temp=[]
            while left<=mid and right<=high:
                if nums[left]<=nums[right]:
                    temp.append(nums[left])
                    left+=1
                else:
                    temp.append(nums[right])
                    right+=1
            #remaining elements for longer arr
            while left<=mid:
                temp.append(nums[left])
                left+=1
            while right<=high:
                temp.append(nums[right])
                right+=1
            for i in range(low,high+1):
                nums[i]=temp[i-low]
        mergeSort(nums,0,len(nums)-1)
        return nums
