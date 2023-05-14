class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # Initialize variables
        char_dict = {}  # Dictionary to store the last seen index of each character
        left, right, max_len = 0, 0, 0  # Pointers and maximum length of substring
        
        # Iterate until the right pointer reaches the end of the string
        while right < len(s):
            # If the character at the right pointer is not in the dictionary
            if s[right] not in char_dict:
                char_dict[s[right]] = right  # Add the character and its index to the dictionary
                right += 1  # Move the right pointer one position to the right
            # If the character at the right pointer is already in the dictionary and its index is within the current substring
            elif char_dict[s[right]] >= left:
                left = char_dict[s[right]] + 1  # Move the left pointer to the index of the last seen occurrence of that character + 1
                char_dict[s[right]] = right  # Update the last seen index of the character to the current position of the right pointer
                right += 1
            else:
                char_dict[s[right]] = right
                right += 1
                
            max_len = max(max_len, right - left)  # Update the maximum length of the substring
            
        return max_len
