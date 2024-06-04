class Solution {
public:
    bool isPalindrome(string s) {
        // if(s.size() == 1){
        //     return true;
        // }
        for(int i = 0; i < s.size(); i++){
            if(isdigit(s[i])){
                continue;
            }
            else if(isalpha(s[i])){
                s[i] = tolower(s[i]);
            }
            else if (!isalpha(s[i]) || s[i] == ' '){
                s.erase(s.begin()+i);
                i--;
            }
        }

        bool status = true;
        int start = 0;
        int end = s.size()-1;

        // trying two pointer aproach basic...
        while(start <= end){
            if(s[start] != s[end]){
                status = false;
                return status;
            }
            else{
                start++;
                end--;
            }
        }
    
        return status;
    }
};