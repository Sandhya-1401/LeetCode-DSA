class Solution(object):
    def rotate(self, nums, k):

        n = len(nums)
        k = k % n  # Handle cases where k > n
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)
    
    def reverse(self, nums, left, right):
        """Helper function to reverse elements in-place"""
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

nums = [1,2,3,4,5,6,7]
k = 3
sol = Solution()
sol.rotate(nums, k)
print(nums)  
