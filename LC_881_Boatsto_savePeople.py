class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        l=0
        b=0
        r=len(people)-1
        while l<=r:
            if people[l]+people[r]<=limit:
                r=r-1
            l=l+1
            b=b+1
        return b

        
