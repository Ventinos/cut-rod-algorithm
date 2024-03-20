import random

def max(a, b):
    if a > b:
        return a
    return b

def cut_rod(p, n):
    if n == 0:
        return 0

    q = -1
    for i in range(1, n+1):
        q = max(q, p[i] + cut_rod(p, n-i))

    return q

def memoized_cut_rod(p, n):
    r = [-1 for _ in range(0,n+1)]
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

def bottom_up_cut_rod(p, n):
    r = [i for i in range(0, n+1)]

    for j in range(1, n+1):
        q = -1
        for i in range(1, j+1):
            q = max(q, p[i] + r[j - i])
        r[j] = q

    return r[n]

def extended_bottom_up_cut_rod(p, n):
    r = [i for i in range(0, n+1)]
    s = [i for i in range(1, n+2)]

    for j in range(1, n+1):
        q = -1
        for i in range(1, j+1):
            if q < p[i] + r[j - i]:
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
    #TODO: ajustar todas os metodos para aceitar n maiores que len(p)
    p = [0, 1, 5, 8, 9, 10, 17, 20, 24, 30]
    #Esse eh um jeito de criar uma tabela desafiadora de precos:
    p1 = [random.randint(0,10000) for _ in range(0,11)]
    p1[0] = 0

    n = 6
    print(cut_rod(p, n))
    print(memoized_cut_rod(p, n))
    print(bottom_up_cut_rod(p, n))
    print(extended_bottom_up_cut_rod(p, n))

if __name__=='__main__':
    main()
