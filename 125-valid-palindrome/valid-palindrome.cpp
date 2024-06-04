class Solution {
public:
    bool isPalindrome(string s) {
        bool status = false;
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

        string rev = s;

        cout << s << endl;

        reverse(rev.begin(), rev.end());

        return rev == s ? true : false;
    }
};