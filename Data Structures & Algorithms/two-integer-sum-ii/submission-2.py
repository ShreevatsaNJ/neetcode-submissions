# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         for i in range(len(numbers)):
#             for j in range(i+1,len(numbers)):
#                 if numbers[i]+numbers[j]==target:
#                     return [numbers[i],numbers[j]]
#         else:
#             return -1

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            
            if curr_sum == target:
                # +1 because problem requires 1-indexed output
                return [left + 1, right + 1]
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
