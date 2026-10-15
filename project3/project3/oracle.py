import urllib.request
import urllib.parse
import base64

def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

def query(student_id):
    data = urllib.parse.urlencode({"student_id": student_id}).encode()
    req = urllib.request.Request("https://l4.neucrypt.org/project3", data=data)
    with urllib.request.urlopen(req) as resp:
        return resp.read().decode()

ids_to_test = ["AAAAAAAAAAAAAAAA", "BBBBBBBBBBBBBBBB", "0123456789ABCDEF"]

keys = []
for sid in ids_to_test:
    assert len(sid) == 16, f"{sid!r} is not 16 chars"
    raw = query(sid)
    print("raw response:", repr(raw))

    line = raw.strip()
    prefix = "Encrypted message: "
    if line.startswith(prefix):
        line = line[len(prefix):]
    blocks_b64 = line.split()

    ct0 = base64.b64decode(blocks_b64[0])
    k0 = xor(ct0, sid.encode())
    print(f"{sid} -> key0 = {k0.hex()}")
    keys.append(k0)
    print()

print("all match:", all(k == keys[0] for k in keys))
