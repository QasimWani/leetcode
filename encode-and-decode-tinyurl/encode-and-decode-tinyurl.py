class Codec:
    def __init__(self):
        self.database = {}#hash id : long_url
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        #hash it
        P = 10000019 #set hash prime
        X = 31
        hash = 0
        for char in reversed(longUrl):
            hash += (hash*X + ord(char))%P

        self.database[hash] = longUrl
        return hash

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        #look up from hash
        return self.database[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))