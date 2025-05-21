class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l=0
        ans=0
        d=dict()
        for r in range(0,len(fruits)):
            val=fruits[r]
            d[val]=d.get(val,0)+1
            while len(d)>2:
                lval=fruits[l]
                d[lval]=d[lval]-1
                if d[lval]==0:
                    del d[lval]
                l+=1
            ans=max(ans,r-l+1)
        return ans



        
