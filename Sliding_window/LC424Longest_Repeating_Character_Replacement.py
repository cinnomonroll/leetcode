# ou are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.



class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        result = 0

        left = 0
        max_freq = 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            max_freq = max(max_freq, count[s[right]])

            while (right - left + 1) - max(count.values()) > k: 
                # shift left pointer
                count[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result
    

solution = Solution()

# Test cases
test_cases = [
    ("ABAB", 2),      
    ("AABABBA", 1),   
    ("AAAA", 0),      
    ("ABBB", 1),      
]

# Run test cases
for s, k in test_cases:
    result = solution.characterReplacement(s, k)
    print(f"Input: s = \"{s}\", k = {k}")
    print(f"Output: {result}\n")