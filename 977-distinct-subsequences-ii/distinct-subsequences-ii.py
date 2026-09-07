class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        
        dp = [0] * (len(s) + 1)
        dp[0] = 1   # empty subsequence
        
        last = [-1] * 26
        
        for i in range(1, len(s) + 1):
            ch = ord(s[i - 1]) - ord('a')
            
            # Every existing subsequence can either take this character or not
            dp[i] = (2 * dp[i - 1]) % MOD
            
            # If this character appeared before, remove duplicates
            if last[ch] != -1:
                dp[i] = (dp[i] - dp[last[ch] - 1]) % MOD
            
            last[ch] = i
        
        # Remove empty subsequence
        return (dp[len(s)] - 1) % MOD