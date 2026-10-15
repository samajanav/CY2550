import urllib.request, urllib.parse

def query(student_id):
    data = urllib.parse.urlencode({"student_id": student_id}).encode()
    req = urllib.request.Request("https://l4.neucrypt.org/project3", data=data)
    with urllib.request.urlopen(req) as resp:
        return resp.read().decode()

# does it accept special characters like | and :  ?
print(query("| Grade: 10     "))   # must be exactly 16 chars

# does it accept a short id and pad it, or does it need exactly 16?
print(query("abc"))
