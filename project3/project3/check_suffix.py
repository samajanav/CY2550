import base64

def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

ct1 = base64.b64decode("EWHE5Xusp93kUTpZZUbx0Q==")

# we don't have a confirmed key1 yet, so instead let's just decrypt block1
# using candidate keys derived differently -- but we actually need key1 itself.
# Since we don't have confirmed key1, print raw block1 so we can inspect:
print(ct1.hex())
