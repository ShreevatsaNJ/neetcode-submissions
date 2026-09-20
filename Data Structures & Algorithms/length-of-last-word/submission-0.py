class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        t=s.strip()
        lst=list((t).split(" "))
        m=lst[-1]
        return len(m)