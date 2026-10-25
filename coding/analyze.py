"""Agreement and derived classes for the five-function test.

Usage: python3 analyze.py coder_a.csv coder_b.csv [human.csv]
Each CSV: slug,F1,F2,F3,F4,F5,SUFF  (codes 0/1/2; SUFF = 1 if the coder judges the
sufficiency rule met, else 0). Classes follow PREREGISTRATION.md section 4.
"""
import csv
import sys
from collections import Counter

FUNCS = ["F1", "F2", "F3", "F4", "F5"]


def load(path):
    with open(path) as f:
        return {r["slug"]: {k: int(r[k]) for k in FUNCS + ["SUFF"]} for r in csv.DictReader(f)}


def derive(c):
    if all(c[f] == 2 for f in FUNCS) and c["SUFF"] == 1:
        return "learning_os"
    if c["F2"] == 2 and c["F5"] == 2:
        return "external_platform"
    if (c["F1"] >= 1 or c["F3"] >= 1) and c["F5"] < 2:
        return "internal_platform"
    return "single_application"


def kappa(a, b, weighted=False, cats=None):
    cats = cats or sorted(set(a) | set(b))
    n = len(a)
    idx = {c: i for i, c in enumerate(cats)}
    k = len(cats)

    def w(i, j):
        if not weighted:
            return 1.0 if i == j else 0.0
        return 1 - abs(i - j) / (k - 1) if k > 1 else 1.0

    po = sum(w(idx[x], idx[y]) for x, y in zip(a, b)) / n
    pa, pb = Counter(a), Counter(b)
    pe = sum(w(idx[x], idx[y]) * pa[x] * pb[y] for x in cats for y in cats) / n**2
    return ((po - pe) / (1 - pe) if pe < 1 else float("nan")), po  # nan: no variance, kappa undefined


def compare(x, y, label):
    common = sorted(set(x) & set(y))
    print(f"\n== {label}: n={len(common)}")
    for f in FUNCS:
        a = [x[s][f] for s in common]
        b = [y[s][f] for s in common]
        ku, po = kappa(a, b, cats=[0, 1, 2])
        kw, _ = kappa(a, b, weighted=True, cats=[0, 1, 2])
        print(f"{f}: agree={po:.2f} kappa={ku:.2f} weighted={kw:.2f}")
    ca = [derive(x[s]) for s in common]
    cb = [derive(y[s]) for s in common]
    kc, po = kappa(ca, cb)
    print(f"class: agree={po:.2f} kappa={kc:.2f}")
    return [(s, f, x[s][f], y[s][f]) for s in common for f in FUNCS if x[s][f] != y[s][f]]


if __name__ == "__main__":
    a, b = load(sys.argv[1]), load(sys.argv[2])
    dis = compare(a, b, "Coder A vs Coder B")
    print(f"\nDisagreements (A vs B): {len(dis)}")
    for d in dis:
        print(*d, sep=",")
    print("\nClasses (A / B):")
    for s in sorted(a):
        print(s, derive(a[s]), derive(b.get(s, a[s])), sep=",")
    if len(sys.argv) > 3:
        h = load(sys.argv[3])
        compare(h, a, "Human vs Coder A")
        compare(h, b, "Human vs Coder B")
