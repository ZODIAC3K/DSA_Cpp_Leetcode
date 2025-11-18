class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        // below solution preserves the history which is bad for memory
        // 1 → [0, 3]
        // 2 → [1, 4]
        // 3 → [2, 5]
    //     HashMap<Integer, ArrayList<Integer>> map = new HashMap<>();
    //     for (int i = 0; i < nums.length; i++) {
    //         if (!map.containsKey(nums[i])) {
    //             ArrayList<Integer> list = new ArrayList<>();
    //             list.add(i);
    //             map.put(nums[i], list); // adds new arraylist with i in it and put it in map with key
    //             continue;
    //         }

    //         map.get(nums[i]).add(i);

    //         ArrayList<Integer> data = map.get(nums[i]);
    //         int secondLast = data.get(data.size() - 2);

    //         if (Math.abs(i - secondLast) <= k) {
    //             // because most recent will be bigger but we have abs so not required to be honest.
    //             return true;
    //             // returns for any value which full fills above if condition.
    //         }

    //     }
    //     return false;
    // }
        // HashMap<Integer, Integer> map = new HashMap<>();
        // for (int i = 0; i < nums.length; i++) {
        //     if (!map.containsKey(nums[i])) {
        //         map.put(nums[i], i);
        //         continue;
        //     }
        //     int lastValue = map.get(nums[i]);
        //     if ((i - lastValue) <= k) {
        //         return true;
        //     }
        //     map.put(nums[i], i);
        // }
        // return false;


        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            Integer prev = map.put(nums[i], i); // return null if no value was there and puts in new value
            if (prev != null && i - prev <= k) {
                return true;
            }
        }
        return false;
    }
}