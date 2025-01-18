class Solution:
    def scoreOfString(self, s: str) -> int:
        # store in score
        score = 0
        diff = 0
        # traverse the string
        for i in range(0, len(s) - 1):
            score = score + abs(ord(s[i]) - ord(s[i + 1]))
        return score
