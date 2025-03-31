class Solution {
    public int longestOnes(int[] nums, int k) {
        int l=0,ans=0,temp=0;
        for(int r=0;r<nums.length;r++){
            if(nums[r]==0){
                temp++;
            }
            while(temp>k){
                if(nums[l]==0){
                    //nums[l]=1;
                    temp--;
                }
                l++;
            }
            ans=Math.max(ans,r-l+1);
        }
        return ans;
    }
}
