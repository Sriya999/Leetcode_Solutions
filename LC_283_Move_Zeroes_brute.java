class Solution {
    public void moveZeroes(int[] nums) {

        ArrayList<Integer> temp = new ArrayList<>();
        //TC---O(2N)
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                temp.add(nums[i]);
            }
        }
        System.out.println(temp);
        // add non zeroes to nums[]
        for (int j = 0; j < temp.size(); j++) {
            nums[j] = temp.get(j);
        }
        for (int j = temp.size(); j < nums.length; j++) {
            nums[j] = 0;
        }

        for (int k = 0; k < nums.length; k++) {
            System.out.print(nums[k] + " ");
        }

    }
}
