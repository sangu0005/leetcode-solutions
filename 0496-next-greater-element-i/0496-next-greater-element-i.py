class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1idx = {}
        for i in range(len(nums1)):
            nums1idx[nums1[i]] = i
        
        res = [-1] * len(nums1)

        for i in range(len(nums2)):
            if nums2[i] not in nums1idx:
                continue
            
            for j in range(i+1, len(nums2)):
                if nums2[j] > nums2[i]:
                    idx = nums1idx[nums2[i]]
                    res[idx] = nums2[j]
                    break
        return res




            
