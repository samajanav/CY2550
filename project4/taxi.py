import hashlib, itertools, string, sys

rows = [l.strip().split(',') for l in open(sys.argv[1]) if l.strip()]
med_hashes = {r[0].upper() for r in rows}
lic_hashes = {r[1].upper() for r in rows}

def md5(s):
    return hashlib.md5(s.encode()).hexdigest().upper()  # no trailing newline

U, D = string.ascii_uppercase, string.digits

def medallions():
    for d1, l, d2, d3 in itertools.product(D, U, D, D):
        yield d1 + l + d2 + d3                       # 5X55
    for a, b, n in itertools.product(U, U, itertools.product(D, repeat=3)):
        yield a + b + ''.join(n)                     # XX555
    for a, b, c, n in itertools.product(U, U, U, itertools.product(D, repeat=3)):
        yield a + b + c + ''.join(n)                 # XXX555

medallion = next((m for m in medallions() if md5(m) in med_hashes), None)
if medallion is None:
    sys.exit("No medallion found - check that the file downloaded correctly")

licenses = [str(n) for n in itertools.chain(
    (f"{i:06d}" for i in range(1_000_000)),          # 6 digits
    range(5_000_000, 6_000_000))                     # 7 digits starting with 5
    if md5(str(n)) in lic_hashes]

with open("taxi.txt", "w") as f:
    f.write(medallion + "\n")
    f.write("\n".join(licenses) + "\n")
print(medallion, licenses)
