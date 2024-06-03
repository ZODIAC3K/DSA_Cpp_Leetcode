class Solution {
public:
    bool isPalindrome(int x) {
        int original = x;
        int rev = 0;
        if(x<0){
            return false;
        }
        while(x>0){
            int rem = x % 10;
            if (rev > INT_MAX / 10 || (rev == INT_MAX / 10 && rem > 7)) return false;
            rev = rev * 10 + rem;
            x = x / 10;
        }
        return (original == rev)? true : false;
    }
};