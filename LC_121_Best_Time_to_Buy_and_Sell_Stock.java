class Solution {
    public int maxProfit(int[] prices) {
        int buy_price = prices[0];
        int max_Profit = 0;
        for (int i = 0; i < prices.length; i++) {
            int cost = prices[i] - buy_price;
            max_Profit = Math.max(max_Profit, cost);
            buy_price = Math.min(buy_price, prices[i]);
        }
        return max_Profit;
    }
}
