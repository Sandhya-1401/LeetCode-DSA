class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Merge nums2 into nums1 as a single sorted array in-place.
        
        :param nums1: List[int] - First sorted array (with extra space at the end).
        :param m: int - Number of elements in nums1.
        :param nums2: List[int] - Second sorted array.
        :param n: int - Number of elements in nums2.
        """
        # Pointers for nums1, nums2, and the last position in nums1
        p1, p2, p = m - 1, n - 1, m + n - 1

        # Traverse from the end and place the largest element at the end of nums1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1  # Move the pointer in nums1

        # If nums2 still has remaining elements, copy them to nums1
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
