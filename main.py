from random import randint
from time import time

# auxiliar methods:
def max(a, b):
    if a > b:
        return a
    return b

# top-bottom naive recursive implementation:
def cut_rod(p, n):
    if n == 0:
        return 0

    q = -1
    for i in range(1, n+1):
        if(i < len(p)):
            q = max(q, p[i] + cut_rod(p, n-i))
        else:
            q = max(q, cut_rod(p, i) + cut_rod(p, n-i))

    return q

# top-down with memoization implementation:
def memoized_cut_rod(p, n):
    r = [-1]*(n+1)
    return memoized_cut_rod_aux(p, n, r)

def memoized_cut_rod_aux(p, n, r):
    if r[n] >= 0:
        return r[n]

    if n == 0:
        q = 0
    else:
        q = -1
        for i in range(1, n+1):
            if(i < len(p)):
                q = max(q, p[i] + memoized_cut_rod_aux(p, n-i, r))
            else:
                q = max(q, memoized_cut_rod_aux(p, i, r) + memoized_cut_rod_aux(p, n-i, r))

    r[n] = q
    return q

# bottom-up implementation:
def bottom_up_cut_rod(p, n):
    r = list(range(0, n+1))

    for j in range(1, n+1):
        q = -1
        for i in range(1, j+1):
            if(i < len(p)):
                q = max(q, p[i] + r[j - i])
            else:
                q = max(q, r[i] + r[j - i])
        r[j] = q

    return r[n]

# reconstruction of the optimal solution:
def extended_bottom_up_cut_rod(p, n):
    r = list(range(0, n+1))
    s = list(range(1, n+2))

    for j in range(1, n+1):
        q = -1
        for i in range(1, j+1):
            if(q < p[i] + r[j - i]):
                q = p[i] + r[j - i]
                s[j] = i
        r[j] = q

    return r,s

def print_cut_rod_solution(p, n):
    r, s = extended_bottom_up_cut_rod(p, n)

    while n > 0:
        print(s[n])
        n = n - s[n]

def main():
    #TODO: arrumar cut_rod(p, n)
    p = [0, 1, 5, 8, 9, 10, 17, 20, 24, 30]
    p1 = [0, 2, 1, 3]
    rand_p = [randint(0,10000) for _ in range(0,50)]
    rand_p[0] = 0
    #for n in range(0, 1001):
        #start = time()
    print(bottom_up_cut_rod(p, 4))
        #end = time()
        #print(end - start)


if __name__=='__main__':
    main()
