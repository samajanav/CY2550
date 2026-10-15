import base64

def xor(a, b):
   return bytes(x ^ y for x, y in zip(a, b))

blocks_b64 = [
    "PASTE_FIRST_BLOCK_HERE",
    "PASTE_SECOND_BLOCK_HERE",
]
student_id = "AB1234567890CD1234567890EFGHIJKL"   # exactly what you sent

blocks = [base64.b64decode(b) for b in blocks_b64]
pt = student_id.encode()
assert len(pt) == 32, "id must be exactly 32 bytes"

for i in range(0, 32, 16):
    k = xor(blocks[i // 16], pt[i:i+16])
    print(f"block {i//16}: key = {k.hex()}")
