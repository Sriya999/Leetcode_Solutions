class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count=0
        for i in range(0,len(stones)):
            for j in range(0,len(jewels)):
                if jewels[j]==stones[i]:
                    count=count+1
        return count
       