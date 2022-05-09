package Java;

import java.util.*;

// Time: O(n log(n))
// Space: O(n)
class Program {

    public int[] sortedSquaredArray(int[] array) {
        int[] list = new int[array.length];

        for (int i = 0; i < array.length; i++) {
            int x = array[i] * array[i];
            list[i] = x;
        }

        Arrays.sort(list);
        return list;
    }
}

class Program2 {
    public int[] sortedSquaredArray(int[] array) {
        int[] sortedArray = new int[array.length];
        int smallerValueIdx = 0;
        int largerValueIdx = array.length - 1;

        for (int i = array.length - 1; i >= 0; i--) {
            int smallerValue = array[smallerValueIdx];
            int largerValue = array[largerValueIdx];

            if (Math.abs(smallerValue) > Math.abs(largerValue)) {
                sortedArray[i] = smallerValue * smallerValue;
                smallerValueIdx++;
            } else {
                sortedArray[i] = largerValue * largerValue;
                largerValueIdx--;
            }
        }
        return sortedArray;
    }
}