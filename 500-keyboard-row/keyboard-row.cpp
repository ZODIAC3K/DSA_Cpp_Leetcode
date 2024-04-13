class Solution {
public:
    vector<string> findWords(vector<string>& words) {
        string first_row = "qwertyuiop", second_row = "asdfghjkl",
               third_row = "zxcvbnm";
        vector<string> result;

        for (int i = 0; i < words.size(); i++) {
            bool first = true, second = true, third = true;
            for (int word = 0; word < words[i].size(); word++) {
                char current_char = tolower(words[i][word]);
                if (first_row.find(current_char) == string::npos) {
                    first = false;
                    break;
                }
            }
            if (first) {
                result.push_back(words[i]);
                continue;
            }

            for (int word = 0; word < words[i].size(); word++) {
                char current_char = tolower(words[i][word]);
                if (second_row.find(current_char) == string::npos) {
                    second = false;
                    break;
                }
            }
            if (second) {
                result.push_back(words[i]);
                continue;
            }

            for (int word = 0; word < words[i].size(); word++) {
                char current_char = tolower(words[i][word]);
                if (third_row.find(current_char) == string::npos) {
                    third = false;
                    break;
                }
            }
            if (third) {
                result.push_back(words[i]);
            }
        }

        return result;
    }
};