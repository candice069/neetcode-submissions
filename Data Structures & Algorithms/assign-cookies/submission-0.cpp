class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        int index = 0;
        int res = 0;
        
        while(res < g.size() and index < s.size()){
            if (g[res] <= s[index]){
                res+=1;
            }
            index += 1;
        }
        return res;
    }
};