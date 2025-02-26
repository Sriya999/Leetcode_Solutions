class Solution {
    public boolean validmat(int matrix[][], int y, int x) {
        // if diagonal ele are same
        int i = y;
        int j = x;
        int r = matrix.length;
        int c = matrix[0].length;
        boolean isvalid = true;
        int temp = matrix[i][j];
        while (i < r && j < c) {
            if (temp != matrix[i][j]) {
                isvalid = false;
                break;
            }
            i++;
            j++;
        }
        return isvalid;
    }

    public boolean isToeplitzMatrix(int[][] matrix) {

        int r = matrix.length;
        int c = matrix[0].length;
        boolean ans = true;
        // passing first row indices
        for (int i = 0; i < c; i++) {
            ans = validmat(matrix, 0, i);
            if (ans == false) {
                return false;
            }
        }

        // passing first col indices
        for (int j = 0; j < r; j++) {
            ans = validmat(matrix, j, 0);
            if (ans == false) {
                return false;
            }
        }
        return ans;
    }
}
