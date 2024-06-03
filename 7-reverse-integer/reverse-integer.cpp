class Solution {
public:
    int reverse(int x) {
        int originalNum = x;
        int rev = 0;
        bool isNeg = false;
        if(x < 0){
            x = abs(x);
            isNeg = true; 
        }
        while(x > 0){
            int rem = x % 10;
            if (rev > INT_MAX / 10 || (rev == INT_MAX / 10 && rem > 7)) return 0;
            rev = rev * 10 + rem;
            x = x / 10;
        }
        if(isNeg == true){
            return 0 - rev;
        }else{
            return rev;
        }

        
    }
};