package Java;

import java.util.*;

// Time: O(n^2)
// Space: O(n)
class Program {
    public static List<Integer[]> threeNumberSum(int[] array, int targetSum) {
        Arrays.sort(array);
        ArrayList<Integer[]> list = new ArrayList<>();

        for (int i = 0; i < array.length - 2; i++) {
            int left = i + 1;
            int right = array.length - 1;

            while (left < right) {
                int currentSum = array[i] + array[left] + array[right];

                if (currentSum == targetSum) {
                    Integer[] ans = { array[i], array[left], array[right] };
                    list.add(ans);
                    left++;
                    right--;
                }

                else if (currentSum < targetSum) {
                    left++;
                }

                else if (currentSum > targetSum) {
                    right--;
                }
            }
        }
        return list;
    }
}
