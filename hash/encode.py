class Codec:
    def __init__(self):
        self.url_to_code = {}
        self.code_to_url = {}
        self.base_url = "http://tinyurl.com/"
        self.counter = 0

    def encode(self, longUrl: str) -> str:
        if longUrl in self.url_to_code:
            return self.base_url + self.url_to_code[longUrl]

        short_code = str(self.counter)
        self.url_to_code[longUrl] = short_code
        self.code_to_url[short_code] = longUrl
        self.counter += 1

        return self.base_url + short_code

    def decode(self, shortUrl: str) -> str:
        short_code = shortUrl.replace(self.base_url, "")
        return self.code_to_url.get(short_code, "")

# Example usage:
url_encoder_decoder = Codec()
long_url = "https://leetcode.com/problems/design-tinyurl"
encoded_url = url_encoder_decoder.encode(long_url)
decoded_url = url_encoder_decoder.decode(encoded_url)

print(f"Original URL: {long_url}")
print(f"Encoded URL: {encoded_url}")
print(f"Decoded URL: {decoded_url}")
