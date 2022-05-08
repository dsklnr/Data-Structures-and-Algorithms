package Java;

import java.util.*;

class Program {
    public static boolean isValidSubsequence(List<Integer> array, List<Integer> sequence) {
        int idx = 0;

        for (int i : array) {
            if (idx == sequence.size()) {
                break;
            }

            if (sequence.get(idx).equals(i)) {
                idx++;
            }
        }
        return idx == sequence.size();
    }
}
