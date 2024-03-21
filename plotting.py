import pandas as pd
import matplotlib.pyplot as plt

def length_time_plot(filename):
    # Reading Data From CSV
    df = pd.read_csv('./data/' + filename, delimiter=';')

    # Extracting Columns from CSV
    length = df['length']
    time = df['time']

    # Plotting it:
    plt.figure(figsize=(10, 6))
    plt.plot(length, time, marker='o', color='b', linestyle='-')

    plt.title('Comprimento vs Tempo de Execução\n' + filename)
    plt.xlabel('Comprimento')
    plt.ylabel('Tempo de Execução')
    plt.grid(True)
    plt.show()

def length_revenue_plot(filename):
    # Reading Data From CSV
    df = pd.read_csv('./data/' + filename, delimiter=';')

    # Extracting Columns from CSV
    length = df['length']
    time = df['revenue']

    # Plotting it:
    plt.figure(figsize=(10, 6))
    plt.plot(length, time, marker='o', color='b', linestyle='-')

    plt.title('Comprimento vs Receita Máxima\n' + filename)
    plt.xlabel('Comprimento')
    plt.ylabel('Receita Máxima')
    plt.grid(True)
    plt.show()

# Função para plotar os pontos do arquivo CSV
def plot_csv(file_path, label):
    df = pd.read_csv('./data/'+file_path, delimiter=';')
    length = df['length']
    time = df['time']
    plt.plot(length, time, marker='o', linestyle='-', label=label)

def length_time_comparisson_plot(filename1, filename2):
    # Comparisson plot:
    plot_csv(filename1, label='Naive')

    plot_csv(filename2, label='Bottom-Up')

    plt.title('Tempo vs Comprimento\n'+filename1+' X '+filename2)
    plt.xlabel('Comprimento')
    plt.ylabel('Tempo')
    plt.legend()
    plt.grid(True)

    plt.savefig('./imgs/'+filename1 + ' X ' + filename2 + '.png', dpi=300)
    plt.clf()

length_time_comparisson_plot('naive_p_rand.csv', 'bottom_up_p_rand.csv')
