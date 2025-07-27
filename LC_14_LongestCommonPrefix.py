class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #take first word and then compare with other words if letters are matching by column
        for i in range(len(strs[0])):
            for string in strs[1:]:
                if  i>=len(string) or string[i]!=strs[0][i]:
                    return strs[0][:i]
        return strs[0]
