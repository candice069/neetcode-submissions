class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        //use pointers
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);

        for(int i = 0; i < nums.length - 3; i++){
            if(i > 0 && nums[i] == nums[i-1]){
                continue;
            }
            if(nums[i] > target && nums[i] > 0){
                break;
            }
            for (int j = i+1; j< nums.length -2; j++){
                if(j> i +1 && nums[j] == nums[j-1]){
                    continue;
                }
                
                int left = j+1;
                int right = nums.length - 1;
                while(left < right){
                    long s = (long)nums[i] + nums[j] + nums[left] + nums[right];
                    if (s == target){
                        res.add(Arrays.asList(nums[i], nums[j], nums[left], nums[right]));
                        left ++;
                        right --;
                        while(left < right && nums[left] == nums[left - 1]){
                            left++;
                        }
                        while(left < right && right < nums.length - 1 && nums[right] == nums[right + 1]){
                            right--;
                        }
                        
                    }else if(s > target){
                        right --;
                    }else{
                        left ++;
                    }
                }
            }

        }
        return res;
    }
}