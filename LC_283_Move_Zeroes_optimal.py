class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        j = -1
        # find j index at first zero
        for i in range(0, len(nums)):
            if nums[i] == 0:
                j = i
                break
        # if no zeroes found return orginal array
        if j == -1:
            return
#if nonzero element encounters swapping it with zero element which is at j index
        for i in range(j + 1, len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j = j + 1

        print(nums)
