class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # Step 1: Calculate the frequency of each character in the string
        freq = Counter(s)
        
        # Step 2: Determine the number of unique characters in the string
        unique_char_count = len(freq)
        
        # Initialize the variable to keep track of the maximum length of valid substring
        max_sub_len = 0

        # Step 3: Iterate over possible unique character counts in the substring
        for num_unique_chars in range(1, unique_char_count + 1):
            # Use a dictionary to count characters in the current window
            char_count = defaultdict(int)
            left = 0
            right = 0
            # Step 4: Expand the right end of the window over the string
            while right < len(s):
                # Add the current character to the count
                char_count[s[right]] += 1
                
                # Step 5: If the number of unique characters exceeds the allowed number, shrink the window from the left
                while len(char_count) > num_unique_chars:
                    char_count[s[left]] -= 1
                    if char_count[s[left]] == 0:
                        del char_count[s[left]]
                    left += 1
                
                # Step 6: Check if all characters in the window meet the frequency requirement
                all_counts_meet_requirement = True
                for count in char_count.values():
                    if count < k:
                        all_counts_meet_requirement = False
                        break
                
                if all_counts_meet_requirement:
                    # Update the maximum length of a valid substring found
                    max_sub_len = max(max_sub_len, right - left + 1)

                right += 1
        # Step 7: Return the maximum length of valid substring
        return max_sub_len
