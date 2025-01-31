class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        count=0
        for i in range(0,len(words)):
            s=str(words[i])
            for j in range(i+1,len(words)):
                if words[i]==0:
                   break
                if s[::-1]==words[j]:
                    count=count+1
                    words[j]=0
                    break
        return count
                        