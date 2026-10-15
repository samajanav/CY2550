import base64

def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

samples = [
    ("x/a/PGC9ZkGcabaOSm3mRw==", "XXXXXXXXXXXXXXXX"),
    ("0pd43N1pv8c28NsdUxkRDA==", "xxxxxxxxxxxxxxxx"),
    ("WKQVxpmU2ZDmsGgwmJLoKg==", "AB1234567890CDEF"),
]

keys = []
for ct_b64, pt in samples:
    ct = base64.b64decode(ct_b64)
    k = xor(ct, pt.encode())
    keys.append(k)
    print(k.hex())

print("all match:", all(k == keys[0] for k in keys))
