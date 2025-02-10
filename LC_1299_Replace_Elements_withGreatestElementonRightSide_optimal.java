class Solution {
    public int[] replaceElements(int[] arr) {
        int n = arr.length;
        //from back of arr
        int  rightmaxi = -1;
        for (int i = n-1; i >= 0; i--) {
            int prev=arr[i];//keep track of current element
            arr[i] =rightmaxi;//storing maxi
            rightmaxi = Math.max(rightmaxi, prev);//updating maxi
            
        }
        return arr;
    }
}
