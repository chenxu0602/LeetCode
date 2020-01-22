
import random, string


class Codec:

    alphabet = string.ascii_letters + "0123456789"

    def __init__(self):
        self.url2code = {}
        self.code2url = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        code = "".join(random.choice(Codec.alphabet) for _ in range(6))
        if code not in self.code2url:
            self.code2url[code] = longUrl
            self.url2code[longUrl] = code
        return "http://tinyurl.com/" + self.url2code[longUrl]


    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.code2url[shortUrl[-6:]]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
