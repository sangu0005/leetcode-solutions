class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # n = len(arr)
        # if n == 1:
        #     return 0

        # peak = 0

        # for i in range(n-1):
        #     if arr[i] > arr[i+1]:
        #         return i

        l, r = 0, len(arr) - 1

        while l < r:
            mid = (l + r) // 2

            if arr[mid] < arr[mid + 1]:
                l = mid + 1
            else:
                r = mid

        return l
