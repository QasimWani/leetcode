class Solution:
    def defangIPaddr(self, address: str) -> str:
        #Time: O(n)
        #Space: O(1), assuming address is passed as reference
        address = list(address)
        for i in range(len(address)):
            if address[i] == '.':
                address[i] = '[.]'
        return "".join(address)