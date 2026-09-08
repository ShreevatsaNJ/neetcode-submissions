class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        lst=[]
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        max_key=sorted(count,key=count.get,reverse=True)[:k]
        return max_key