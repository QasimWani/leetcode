import string

class Solution:
    def validIPAddress(self, IP: str) -> str:
        #Time: O(N)
        #Space: O(1)
        
        if len(IP.split('.')) == 4:#ipv4
            return self.ipv4(IP.split('.'))
        
        if len(IP.split(':')) == 8:
            return self.ipv6(IP.split(':'))
        
        return 'Neither'
    
    def ipv4(self, ip):
        chars = '0123456789'
        for x in ip:
            #check for valid digits
            if any(char not in chars for char in x):
                return 'Neither'
            if x and int(x) <= 255:
                if int(x) == 0 and len(x) == 1:
                    continue
                elif int(x) > 0 and x[0] != '0':
                    continue
                else:
                    return 'Neither'
            else:
                return 'Neither'
        return 'IPv4'
    
    def ipv6(self, ip):
        for x in ip:
            if 1 <= len(x) <= 4 and all(c in string.hexdigits for c in x):
                continue
            else:
                return 'Neither'
        return 'IPv6'
                
                
                
                
            