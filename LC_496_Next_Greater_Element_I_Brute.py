class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1idx = {}  # dict to store elem,indeces

        for k, v in enumerate(nums1):
            nums1idx[v] = k  # elem:idx

        ans = [-1] * len(nums1)
        for i in range(len(nums2)):
            if nums2[i] not in nums1idx:
                continue
            for j in range(i + 1, len(nums2)):
                if nums2[i] < nums2[j]:
                    idx = nums1idx[nums2[i]]
                    ans[idx] = nums2[j]
                    break
        return ans
