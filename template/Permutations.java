package template;

import java.util.ArrayList;
import java.util.Arrays;

public class Permutations {

    public static void main(String[] args) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<>();
        ArrayList<Integer> list = new ArrayList<>();
        int[] nums = new int[] { 1, 2, 3, 4, 5, 6 };
        // subsetHelper(result, list, nums, 0);
        // System.out.println(result);

        // with dup
        Arrays.sort(nums);
        subsetHelperWithDup(result, list, nums, 0);
        System.out.println(result);
    }

    private static void subsetHelper(ArrayList<ArrayList<Integer>> result, ArrayList<Integer> list, int[] nums,
            int pos) {
        result.add(new ArrayList<Integer>(list));
        for (int i = pos; i < nums.length; ++i) {
            list.add(nums[i]);
            subsetHelper(result, list, nums, i + 1);
            list.remove(list.size() - 1);
        }
    }

    private static void subsetHelperWithDup(ArrayList<ArrayList<Integer>> result, ArrayList<Integer> list, int[] nums,
            int pos) {
        result.add(new ArrayList<Integer>(list));
        for (int i = pos; i < nums.length; i++) {
            if (i != pos && nums[i] == nums[i - 1]) {
                continue;
            }
            list.add(nums[i]);
            subsetHelper(result, list, nums, i + 1);
            list.remove(list.size() - 1);
        }

    }
}