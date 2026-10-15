import urllib.request, urllib.parse

def query(student_id):
    data = urllib.parse.urlencode({"student_id": student_id}).encode()
    req = urllib.request.Request("https://l4.neucrypt.org/project3", data=data)
    with urllib.request.urlopen(req) as resp:
        return resp.read().decode()

username = "sama.j"   # <-- edit this
padded = username + " " * (16 - len(username))
assert len(padded) == 16, "username too long to pad to 16 — tell me if so"

print(repr(padded))
print(query(padded))
