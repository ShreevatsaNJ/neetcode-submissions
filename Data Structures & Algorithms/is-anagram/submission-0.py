class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count={}
        total={}
        for i in s:
            if i in count:
                count[i]+=1 
            else:
                count[i]=1
        for i in t:
            if i in total:
                total[i]+=1
            else:
                total[i]=1
        return count.items()==total.items()
