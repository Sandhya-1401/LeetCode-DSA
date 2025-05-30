class Solution {
    public int mySqrt(int x) {
        int low = 1;
        int high = x;
        int ans = 0;
        while(low <= high){
            int mid = low + (high - low)/2;
            if(mid*mid==x)
            {
                ans=mid;
                return ans;
            }
            if((long)mid*mid>x){
                high=mid-1;
            }
            else{
                ans=mid;
                low=mid+1;
            }
        }
        return ans;
    }
}