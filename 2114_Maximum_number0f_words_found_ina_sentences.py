class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxwords=0
        for i in sentences:
                l=list(i.split())
                maxwords=max(maxwords,len(l))
            
        return maxwords
