class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        return sum(i & 1 for i in collections.Counter(s).values()) <= k <= len(s)