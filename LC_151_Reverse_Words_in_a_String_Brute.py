class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()#removes extra spaces
        l = list(s.split())#create list of words
        l = l[::-1]
        s1 = " ".join(l)
        return s1
