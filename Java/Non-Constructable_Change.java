package Java;

import java.util.*;

// Time: O(n log(n))
// Space: O(1)
class Program {

    public int nonConstructibleChange(int[] coins) {
        Arrays.sort(coins);
        int totalCoins = 0;

        for (int i : coins) {
            if (i > totalCoins + 1) {
                return totalCoins + 1;
            }
            totalCoins += i;
        }
        return totalCoins + 1;
    }
}
