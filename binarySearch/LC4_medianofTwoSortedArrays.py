# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5


from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        mid = total // 2

        # make sure A is shorter -> reduce binary search range and simpify boundary case 
        if len(A) > len(B):
            A, B = B, A

        left, right = 0, len(A) - 1
        while True:
            i = (left + right) // 2 # A
            j = mid - i - 2 # B "-2"-> index start from 0

            # in case of edge or out od boundary, so need "infinity" val
            # e.g. A = [2] B = [1, 3]

            A_left = A[i] if i >= 0 else float("-infinity")
            A_right = A[i + 1] if (i + 1) < len(A) else float("infinity")
            B_left = B[j] if j >= 0 else float("-infinity")
            B_right = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # partition is correct
            if A_left <= B_right and B_left <= A_right:

                # odd
                if total % 2:
                    return min(A_right, B_right)
                # even
                return (max(A_left, B_left) + min(A_right, B_right)) / 2
            
            elif A_left > B_right:
                right = i - 1
            else:
                left = i + 1

if __name__ == '__main__':
    nums1 = [1, 4, 7, 10, 12]
    nums2 = [3, 5, 11, 22]
    sol = Solution()
    print(sol.findMedianSortedArrays(nums1, nums2))