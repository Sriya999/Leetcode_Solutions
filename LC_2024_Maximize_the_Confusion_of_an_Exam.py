class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l,ans=0,0
        fcount,tcount=0,0
        for r in range(len(answerKey)):
            if answerKey[r]=='F':
                fcount+=1
            if answerKey[r]=='T':
                tcount+=1
            while min(fcount,tcount)>k:
                if answerKey[l]=='F':
                    fcount-=1
                if answerKey[l]=='T':
                    tcount-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans