class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2
        # nums1.extend(nums2)
        nums1.sort()
        # for i in range(1,m+n-1):
        #     if nums1[i-1]>nums1[i]:
        #         nums1[i-1],nums1[i]=nums1[i],nums1[i-1]
        # for i in range(m+n):
        #     if 0 in nums1:
        #         nums1.remove(0)
        # for i in range(n):
        #     if 0 in nums2:
        #         nums2.remove(0)


        