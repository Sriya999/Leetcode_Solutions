class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        import heapq
        heapq.heapify(nums)
        n=len(nums)
        arr=[]
        for i in range(n//2):
            a=heapq.heappop(nums)
            b=heapq.heappop(nums)
            arr.append(b)
            arr.append(a)
        return arr
            

        
