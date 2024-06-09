class Solution {
public:
    int myAtoi(string s) {
       int i = 0, n = s.size();
        
        // Skip leading whitespaces
        while (i < n && s[i] == ' ') {
            i++;
        }

        // Check if the string is empty after removing leading whitespaces
        if (i == n) {
            return 0;
        }

        // Check for the sign
        bool isNeg = false;
        if (s[i] == '-' || s[i] == '+') {
            isNeg = (s[i] == '-');
            i++;
        }

        long long result = 0;
        // Convert characters to integer
        while (i < n && isdigit(s[i])) {
            result = result * 10 + (s[i] - '0');
            if (result > INT_MAX) {
                return isNeg ? INT_MIN : INT_MAX;
            }
            i++;
        }

        // Apply sign
        result = isNeg ? -result : result;

        // Clamp result to INT_MIN and INT_MAX
        if (result < INT_MIN) return INT_MIN;
        if (result > INT_MAX) return INT_MAX;

        return result;
    }
};