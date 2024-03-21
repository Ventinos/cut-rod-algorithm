from random import randint
from time import time

# auxiliar methods:
def max(a, b):
    if a > b:
        return a
    return b

def print_tests(p, filename, method):
    with open(filename, "w") as f:
        print('length', file=f, end=";")
        print('revenue', file=f, end=";")
        print('time', file=f)
        for n in range(0, len(p)):
            start = time()
            r = method(p,n)
            end = time()
            print(n, file=f, end=";")
            print(r, file=f, end=";")
            print(end - start, file=f)


# top-bottom naive recursive implementation:
def cut_rod(p, n):
    if n == 0:
        return 0

    q = -1
    for i in range(1, n+1):
        q = max(q, p[i] + cut_rod(p, n-i))

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
            q = max(q, p[i] + memoized_cut_rod_aux(p, n-i, r))

    r[n] = q
    return q

# bottom-up implementation:
def bottom_up_cut_rod(p, n):
    r = list(range(0, n+1))

    for j in range(1, n+1):
        q = -1
        for i in range(1, j+1):
            q = max(q, p[i] + r[j - i])
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
    p = [0, 1, 5, 8, 9, 10, 17, 20, 24, 30]
    rand_p = [randint(0,10000) for _ in range(0,31)]
    rand_p[0] = 0

    print_tests(p, 'naive_p_book.csv', cut_rod)
    print_tests(p, 'bottom_up_p_book.csv', bottom_up_cut_rod)
    print_tests(rand_p, 'naive_p_rand.csv', cut_rod)
    print_tests(rand_p, 'bottom_up_p_rand.csv', bottom_up_cut_rod)

    with open("used_ps.txt", "w") as f:
        print(p, file=f)
        print(rand_p, file=f)

if __name__=='__main__':
    main()
