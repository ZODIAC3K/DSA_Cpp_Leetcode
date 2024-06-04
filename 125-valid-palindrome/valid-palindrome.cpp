class Solution {
public:
    bool isPalindrome(string s) {
        int start=0;
        int end=s.size()-1;
        while(start<=end){
            if(!isalnum(s[start])){ // this helps us skip space and special character from start
                start++; 
                continue;
            }
            if(!isalnum(s[end])){ // this helps us skip space and special character from back
                end--;
                continue;
            }
            if(tolower(s[start])!=tolower(s[end])){
                return false;
            }
            else{
               start++;
               end--;
            }
       }
       return true;
    }
};