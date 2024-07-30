from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i = 0
    j = 0

    while i < m and j < n:

        if nums1[i] > nums2[j]:
            nums1[i], nums2[j] = nums2[j], nums1[i]
        i += 1
        j += 1

    print(nums1)
    print("\n")
    print(nums2)



nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3


merge(nums1, m, nums2, n)