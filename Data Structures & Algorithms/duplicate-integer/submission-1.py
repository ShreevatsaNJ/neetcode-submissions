class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr=set(nums) # 1 2 3
                      # i/p 1 2 3 3
        return len(nums)!=len(arr) 
        
