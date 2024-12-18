import random  # Importa o módulo random para gerar números aleatórios
import time  # Importa o módulo time para medir o tempo de execução
import pandas as pd  # Importa o pandas para manipulação de dados
import matplotlib.pyplot as plt  # Importa o matplotlib para plotar gráficos

def calcular_pi_sequencial(num_amostras):
    dentro_circulo = 0  # Inicializa o contador de pontos dentro do círculo

    for _ in range(num_amostras):  # Loop para gerar os pontos
        x = random.uniform(0, 1)  # Gera um número aleatório entre 0 e 1 para x
        y = random.uniform(0, 1)  # Gera um número aleatório entre 0 e 1 para y
        if x**2 + y**2 <= 1:  # Verifica se o ponto (x, y) está dentro do círculo unitário
            dentro_circulo += 1  # Incrementa o contador se o ponto estiver dentro do círculo

    return (4 * dentro_circulo) / num_amostras  # Calcula e retorna a estimativa de Pi

# Teste da solução sequencial com diferentes números de amostras
amostras = [1000, 10000, 100000, 500000, 1000000]  # Lista com diferentes números de amostras
tempos = []  # Lista para armazenar os tempos de execução
valores_pi = []  # Lista para armazenar os valores estimados de Pi

for num_amostras in amostras:  # Loop para testar com diferentes números de amostras
    inicio = time.time()  # Marca o início da medição do tempo
    pi_sequencial = calcular_pi_sequencial(num_amostras)  # Chama a função para calcular Pi
    fim = time.time()  # Marca o fim da medição do tempo
    tempos.append(fim - inicio)  # Armazena o tempo de execução
    valores_pi.append(pi_sequencial)  # Armazena o valor estimado de Pi
    print(f"Pi (Sequencial) com {num_amostras} amostras: {pi_sequencial}")  # Imprime o valor estimado de Pi
    print(f"Tempo (Sequencial) com {num_amostras} amostras: {fim - inicio} segundos")  # Imprime o tempo de execução

# Organizar os dados em um DataFrame do pandas
df = pd.DataFrame({
    'Num_Amostras': amostras,  # Número de amostras
    'Tempo_Execucao': tempos,  # Tempo de execução
    'Valor_Pi': valores_pi  # Valor estimado de Pi
})

# Plotar o gráfico
plt.figure(figsize=(10, 5))  # Define o tamanho da figura

# Gráfico do tempo de execução
plt.subplot(1, 2, 1)  # Cria o primeiro subplot
plt.plot(df['Num_Amostras'], df['Tempo_Execucao'], marker='o')  # Plota o gráfico do tempo de execução
plt.xlabel('Número de Amostras')  # Define o rótulo do eixo x
plt.ylabel('Tempo de Execução (s)')  # Define o rótulo do eixo y
plt.title('Tempo de Execução vs Número de Amostras')  # Define o título do gráfico
plt.grid(True)  # Adiciona uma grade ao gráfico

# Gráfico do valor de Pi
plt.subplot(1, 2, 2)  # Cria o segundo subplot
plt.plot(df['Num_Amostras'], df['Valor_Pi'], marker='o')  # Plota o gráfico do valor de Pi
plt.xlabel('Número de Amostras')  # Define o rótulo do eixo x
plt.ylabel('Valor de Pi')  # Define o rótulo do eixo y
plt.title('Valor de Pi vs Número de Amostras')  # Define o título do gráfico
plt.grid(True)  # Adiciona uma grade ao gráfico

plt.tight_layout()  # Ajusta o layout dos subplots para não sobrepor os elementos
plt.show()  # Exibe o gráfico