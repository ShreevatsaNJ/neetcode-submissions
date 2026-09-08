class Solution:
    def validPalindrome(self, s: str) -> bool:
        t=list(s)
        l=0
        r=len(s)-1
        while(l<r):
            t[l],t[r]=t[r],t[l]
            l+=1
            r-=1
        if "".join(t)==s:
            return True

        for i in range(len(s)):
            new_s=s[:i]+s[i+1:]
            p=list(new_s)
            f=0
            l=len(p)-1
            while(f<l):
                p[f],p[l]=p[l],p[f]
                f+=1
                l-=1
            if "".join(p)==new_s:
                return True 
        return False
        