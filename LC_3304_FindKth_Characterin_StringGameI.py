class Solution:
    def kthCharacter(self, k: int) -> str:
        curr='a'
        word="a"
        for i in range(k-1):
            temp=''
            for curr in word:
                nextchar=chr((ord(curr)-ord('a')+1)%26+ord('a'))
                temp=temp+nextchar
            word=word+temp
            if len(word)>=k:
                break
        return word[k-1]
            
        
