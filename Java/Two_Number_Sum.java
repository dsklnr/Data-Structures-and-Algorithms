package Java;

import java.util.*;

// Time: O(n)
// Space: O(n)
class Program {
    public static int[] twoNumberSum(int[] array, int targetSum) {
        HashSet<Integer> set = new HashSet<>();

        for (int i : array) {
            int result = targetSum - i;

            if (set.contains(result)) {
                return new int[] { result, i };
            }

            else {
                set.add(i);
            }
        }

        return new int[0];
    }
}

// Time: O(nlog(n))
// Space: O(1)
class Program2 {
    public static int[] twoNumberSum(int[] array, int targetSum) {
        Arrays.sort(array);

        int left = 0;
        int right = array.length - 1;

        while (left < right) {
            int sum = array[left] + array[right];

            if (sum == targetSum) {
                return new int[] { array[left], array[right] };
            }

            else if (sum < targetSum) {
                left++;
            }

            else if (sum > targetSum) {
                right--;
            }
        }

        return new int[0];
    }
}