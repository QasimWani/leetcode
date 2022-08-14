class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table_s = collections.Counter(s)
        table_t = collections.Counter(t)
        
        for k, v in table_s.items():
            if k not in table_t:
                return False
            if v != table_t[k]:
                return False
            del table_t[k]
        return len(table_t) == 0