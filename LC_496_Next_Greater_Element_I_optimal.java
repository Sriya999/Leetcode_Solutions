class Solution {
    public int[] nextGreaterElement(int[] findNums, int[] nums) {

        Map<Integer, Integer> map = new HashMap<>();
        Stack<Integer> stack = new Stack<>();
        
        for (int i =nums.length- 1; i >= 0; i--) {
            while (!stack.isEmpty() && stack.peek() <= nums[i]) {
                stack.pop();
            }
            if (stack.isEmpty()) {
                map.put(nums[i],-1);

            } else {
                map.put(nums[i],stack.peek());
            }
            stack.push(nums[i]);
        }
          int ans[] = new int[findNums.length];
          for(int j=0;j<findNums.length;j++){
            ans[j]=map.get(findNums[j]);
          }
            return ans;
        
    }
}
