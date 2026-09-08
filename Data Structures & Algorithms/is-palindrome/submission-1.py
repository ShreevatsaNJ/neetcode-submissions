class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = list("".join(i for i in s if i.isalnum())) 
        temp="".join(t).lower()
        l=0
        r=len(t)-1
        while(l<r):
            t[l],t[r]=t[r],t[l]
            l+=1
            r-=1
        if "".join(t).lower()==temp:
            return True
            
        return False
        

        