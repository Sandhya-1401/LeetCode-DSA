class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int low = 0;
        int high = numbers.length - 1;

        while (low < high) {
            int sum = numbers[low] + numbers[high];

            if (sum == target) {
                // Since the problem asks for 1-based indexing
                return new int[] { low + 1, high + 1 };
            } else if (sum < target) {
                low++; // move the left pointer to the right
            } else {
                high--; // move the right pointer to the left
            }
        }

        // If no solution is found (though the problem says there will be one)
        return new int[] {};
    }
}
