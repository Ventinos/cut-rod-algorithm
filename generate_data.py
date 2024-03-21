from algorithms import *
from plotting import *

def main():
    # Book price table:
    #p = [0, 1, 5, 8, 9, 10, 17, 20, 24, 30]
    #print_tests(p, 'naive_p_book.csv', cut_rod)
    #print_tests(p, 'bottom_up_p_book.csv', bottom_up_cut_rod)

    # Random table:
    for n in range(51,1001,100):
        rand_p = [randint(0,10000) for _ in range(0,n)]
        rand_p[0] = 0

        print_tests(rand_p, 'naive_p_rand' + str(n) + '.csv', cut_rod)
        print_tests(rand_p, 'bottom_up_p_rand' + str(n) + '.csv', bottom_up_cut_rod)

        length_time_comparisson_plot('naive_p_rand' + str(n) + '.csv', 'bottom_up_p_rand' + str(n) + '.csv')

        with open("used_ps.txt", "a") as f:
            print(n, file=f, end=";")
            print(rand_p, file=f)

if __name__=='__main__':
    main()
