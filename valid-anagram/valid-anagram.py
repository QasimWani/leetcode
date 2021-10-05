class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # time: O(n log n)
        # space: O(1)
        return sorted(s) == sorted(t)