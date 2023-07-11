def encode(strs):
	return "#".join(strs)  # Using '#' as the delimiter


def decode(s):
	return s.split("#")  # Splitting the encoded string using '#'


strs = ["hello", "world", "coding"]
encoded_str = encode(strs)
print("Encoded string:", encoded_str)

decoded_strs = decode(encoded_str)
print("Decoded strings:", decoded_strs)
