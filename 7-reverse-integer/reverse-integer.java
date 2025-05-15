public class Solution {
    public int reverse(int x) {
        int result = 0;

        while (x != 0) {
            int digit = x % 10;

            // Check for overflow before actually multiplying or adding
            if (result > Integer.MAX_VALUE / 10 || (result == Integer.MAX_VALUE / 10 && digit > 7)) {
                return 0;
            }
            if (result < Integer.MIN_VALUE / 10 || (result == Integer.MIN_VALUE / 10 && digit < -8)) {
                return 0;
            }

            result = result * 10 + digit;
            x /= 10;
        }

        return result;
    }

    // For testing purpose
    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.reverse(123));        // Output: 321
        System.out.println(sol.reverse(-123));       // Output: -321
        System.out.println(sol.reverse(120));        // Output: 21
        System.out.println(sol.reverse(1534236469)); // Output: 0 (overflow)
    }
}
