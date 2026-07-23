class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()

        left = 0
        longest = 0

        for right in range(len(s)):

            while s[right] in seen:
                seen.remove(s[left])
                # remove if found and replace with new one
                left += 1

            seen.add(s[right])

            longest = max(longest, right - left + 1)

        return longest