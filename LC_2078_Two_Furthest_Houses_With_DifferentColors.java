class Solution {
    public int maxDistance(int[] colors) {
        int maxDist = 0;
        for (int i = 0; i < colors.length; i++) {
            for (int j = i + 1; j < colors.length; j++) {
                if (colors[i] != colors[j]) {
                    int dist = Math.abs(i - j);
                    maxDist = Math.max(dist, maxDist);
                }
            }
        }
        return maxDist;
    }
}
