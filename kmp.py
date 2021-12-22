def getnext(s):
    m = len(s)
    next_ind = [0]*m
    k = 0
    for i in range(1, m):
        while k > 0 and s[k] != s[i]:
            k = next_ind[k-1]

        if s[k] == s[i]:
            k += 1

    next_ind[i] = k

    return next_ind

def kmp(s, t):
    n, m = len(s), len(t)
    next_ind = getnext(t)
    q = 0

    for i in range(n):
        while q > 0 and t[q] != s[i]:
            q = next_ind[q-1]

        if t[q] == s[i]:
            q += 1

        if q == m:
            print('found')
            print(i - m + 1)
            q = next_ind[q-1]