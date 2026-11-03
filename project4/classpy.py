import sys
from itertools import product

# usage: python3 classpy.py mu1 m1 mu2 m2 mu3 m3 M3
mu1, m1, mu2, m2, mu3, m3, M3 = map(float, sys.argv[1:8])

AGES = range(17, 22)
out = [f"1:{5**19}"]

def expand(counts):
    return [a for c, a in zip(counts, AGES) for _ in range(c)]

def median(xs):
    xs = sorted(xs); n = len(xs)
    return xs[n // 2] if n % 2 else (xs[n//2 - 1] + xs[n//2]) / 2

# Q2: all sorted age lists matching mean and median of all 19
t1 = round(mu1 * 19)
q2 = []
for n in product(range(20), repeat=5):
    if sum(n) == 19 and sum(c * a for c, a in zip(n, AGES)) == t1:
        ages = expand(n)
        if median(ages) == m1:
            q2.append((n, ages))
out += ["2:" + " ".join(map(str, a)) for _, a in q2]

# Q3: keep those with a 10-person subset matching the on-campus stats
def subsets(n, size):
    for s in product(*(range(c + 1) for c in n)):
        if sum(s) == size:
            yield expand(s)

t2 = round(mu2 * 10)
q3 = [(n, a) for n, a in q2
      if any(sum(s) == t2 and median(s) == m2 for s in subsets(n, 10))]
out += ["3:" + " ".join(map(str, a)) for _, a in q3]

# Q4: keep those with a 3-person subset matching the non-CS stats
t3 = round(mu3 * 3)
q4 = [a for n, a in q3
      if any(sum(s) == t3 and median(s) == m3 and max(s) == M3
             for s in subsets(n, 3))]
out += ["4:" + " ".join(map(str, a)) for a in q4]

open("class.txt", "w").write("\n".join(out) + "\n")
print("\n".join(out))
