class Solution(object):
    def longestPalindrome(self, s):
        # Initialize variables
        n = len(s)
        start = max_len = 0
        
        # Create a 2D DP table to store the results of subproblems
        dp = [[False for _ in range(n)] for _ in range(n)] 

        # Base case: Single characters are palindromes
        for i in range(n):
            dp[i][i] = True
        
        # Initialize the longest palindrome as the first character
        longest = s[0]
        
        # Iterate backwards from the end of the string
        for i in range(n-1, -1, -1):
            # Iterate forwards starting from i+1
            for j in range(i+1, n):
                # Check if the characters at indices i and j are equal
                if s[i] == s[j]:
                    # If the characters are adjacent, they form a palindrome
                    if j - i == 1:
                        dp[i][j] = True
                    # If the characters are not adjacent, check the inner substring
                    else:
                        dp[i][j] = dp[i+1][j-1]
                
                # Check if the substring is a palindrome and longer than the current longest
                if dp[i][j] and j - i + 1 > len(longest):
                    longest = s[i:j+1] 
        
        return longest
