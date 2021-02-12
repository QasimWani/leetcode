class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        #convert jewels into a dictionary and check to see if stones[i] exists in dict(jewels).
        #if so, increment the counter by 1. Simple O(n + k) solution with O(k) space where k = len(jewels)
        jewels = {j: True for j in jewels}
        counter = 0
        for stone in stones:
            if stone in jewels:
                counter += 1
        return counter