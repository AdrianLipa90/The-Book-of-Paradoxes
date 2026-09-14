#!/usr/bin/env python3
"""Deterministic validator for the Banach–Tarski stella-octangula bridge.

No external dependencies.
The bounded free-word search is a finite witness, not a proof of freeness.
"""

V = (
    (1, 1, 1),
    (1, -1, -1),
    (-1, 1, -1),
    (-1, -1, 1),
)

A = (
    (2, -1, 2),
    (-1, 2, 2),
    (-2, -2, 1),
)
B = (
    (2, 1, -2),
    (1, 2, 2),
    (2, -2, 1),
)
DEN = 3

def dot(u, v):
    return sum(a*b for a, b in zip(u, v))

def neg(u):
    return tuple(-x for x in u)

def cross(u, v):
    return (
        u[1]*v[2] - u[2]*v[1],
        u[2]*v[0] - u[0]*v[2],
        u[0]*v[1] - u[1]*v[0],
    )

def mat_t(M):
    return tuple(zip(*M))

def mat_mul(A_, B_):
    BT = tuple(zip(*B_))
    return tuple(tuple(sum(a*b for a,b in zip(row,col)) for col in BT) for row in A_)

def mat_vec(M, v):
    return tuple(sum(a*b for a,b in zip(row,v)) for row in M)

def det3(M):
    (a,b,c),(d,e,f),(g,h,i)=M
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)

I3=((1,0,0),(0,1,0),(0,0,1))

def scale_mat(M, s):
    return tuple(tuple(s*x for x in row) for row in M)

def assert_eq(a,b,msg):
    if a != b:
        raise AssertionError(f"{msg}: {a!r} != {b!r}")

def test_tetrahedral_gram():
    for i,u in enumerate(V):
        assert_eq(dot(u,u), 3, f"norm^2 v{i+1}")
        for j,v in enumerate(V):
            if i != j:
                assert_eq(dot(u,v), -1, f"tetra dot {i+1},{j+1}")
    assert_eq(tuple(map(sum, zip(*V))), (0,0,0), "zero first moment")

def test_stella_spectrum():
    S = V + tuple(neg(v) for v in V)
    spectrum = sorted(set(dot(u,v) for u in S for v in S))
    # normalized by 3 -> {-1,-1/3,+1/3,+1}
    assert_eq(spectrum, [-3,-1,1,3], "stella dot spectrum")

def test_perfect_matching_axes():
    matchings = (((0,1),(2,3)), ((0,2),(1,3)), ((0,3),(1,2)))
    for (i,j),(k,l) in matchings:
        a = cross(V[i], neg(V[j]))
        b = cross(V[k], neg(V[l]))
        assert dot(a,a) > 0 and dot(b,b) > 0
        assert_eq(dot(a,b), 0, f"axis orthogonality {(i+1,j+1)}|{(k+1,l+1)}")

def test_generators():
    assert_eq(mat_mul(mat_t(A), A), scale_mat(I3, DEN*DEN), "A^T A")
    assert_eq(mat_mul(mat_t(B), B), scale_mat(I3, DEN*DEN), "B^T B")
    assert_eq(det3(A), DEN**3, "det(A numerator)")
    assert_eq(det3(B), DEN**3, "det(B numerator)")
    assert_eq(sum(A[i][i] for i in range(3)), 5, "trace A numerator")
    assert_eq(sum(B[i][i] for i in range(3)), 5, "trace B numerator")
    assert_eq(mat_vec(A, V[0]), tuple(-DEN*x for x in V[3]), "A v1 = -v4")
    assert_eq(mat_vec(B, V[1]), tuple(-DEN*x for x in V[2]), "B v2 = -v3")
    axis_A = cross(V[0], neg(V[3]))
    axis_B = cross(V[1], neg(V[2]))
    assert_eq(dot(axis_A, axis_B), 0, "generator axes orthogonal")

def reduced_word_witness(max_len=12):
    gens = {
        "A": A,
        "a": mat_t(A),
        "B": B,
        "b": mat_t(B),
    }
    inv = {"A":"a", "a":"A", "B":"b", "b":"B"}
    total = 0
    identity_hits = 0

    def walk(depth, last, M_num):
        nonlocal total, identity_hits
        if depth == max_len:
            return
        for name,G in gens.items():
            if last is not None and name == inv[last]:
                continue
            next_num = mat_mul(M_num, G)
            n = depth + 1
            total += 1
            if next_num == scale_mat(I3, DEN**n):
                identity_hits += 1
            walk(n, name, next_num)

    walk(0, None, I3)
    expected = 2*(3**max_len - 1)
    assert_eq(total, expected, "reduced word count")
    assert_eq(identity_hits, 0, "bounded identity hits")
    return total

def main():
    test_tetrahedral_gram()
    test_stella_spectrum()
    test_perfect_matching_axes()
    test_generators()
    total = reduced_word_witness(12)
    print("PASS tetrahedral Gram")
    print("PASS stella spectrum")
    print("PASS perfect-matching orthogonal axes")
    print("PASS exact SO(3) generator checks")
    print(f"PASS bounded reduced-word witness: {total} nonempty words, 0 identity hits")
    print("VERDICT: PASS")

if __name__ == "__main__":
    main()
