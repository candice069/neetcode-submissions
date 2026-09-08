class Solution {
private:
    vector<vector<int>> result;
    vector<int> path;
    void backtrack(vector<int>& nums, int start){
        result.push_back(path);
        for(int i = start; i <nums.size(); i ++){
            path.push_back(nums[i]);
            backtrack(nums, i + 1);
            path.pop_back();
        }
    }
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        result.clear();
        path.clear();
        backtrack(nums, 0);
        return result;
    }
};
