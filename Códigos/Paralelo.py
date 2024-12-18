import random  # Importa o módulo random para gerar números aleatórios
import time  # Importa o módulo time para medir o tempo de execução
import threading  # Importa o módulo threading para criar threads
import pandas as pd  # Importa o pandas para manipulação de dados
import matplotlib.pyplot as plt  # Importa o matplotlib para plotar gráficos

def calcular_pi_paralelo(num_pontos, resultados, indice):
    dentro_circulo = 0  # Inicializa o contador de pontos dentro do círculo

    for _ in range(num_pontos):  # Loop para gerar os pontos
        x = random.uniform(0, 1)  # Gera um número aleatório entre 0 e 1 para x
        y = random.uniform(0, 1)  # Gera um número aleatório entre 0 e 1 para y
        if x**2 + y**2 <= 1:  # Verifica se o ponto (x, y) está dentro do círculo unitário
            dentro_circulo += 1  # Incrementa o contador se o ponto estiver dentro do círculo

    resultados[indice] = dentro_circulo  # Armazena o resultado na posição correspondente

# Teste da solução paralela com diferentes números de amostras
amostras = [1000, 10000, 100000, 500000, 1000000]  # Lista com diferentes números de amostras
num_threads = 4  # Define o número de threads
tempos = []  # Lista para armazenar os tempos de execução
valores_pi = []  # Lista para armazenar os valores estimados de Pi

for num_pontos in amostras:  # Loop para testar com diferentes números de amostras
    pontos_por_thread = num_pontos // num_threads  # Divide os pontos igualmente entre as threads
    threads = []  # Lista para armazenar as threads
    resultados = [0] * num_threads  # Lista para armazenar os resultados de cada thread

    inicio = time.time()  # Marca o início da medição do tempo
    for i in range(num_threads):  # Cria e inicia as threads
        thread = threading.Thread(target=calcular_pi_paralelo, args=(pontos_por_thread, resultados, i))
        threads.append(thread)
        thread.start()

    for thread in threads:  # Aguarda todas as threads terminarem
        thread.join()

    dentro_circulo_total = sum(resultados)  # Soma os resultados de todas as threads
    pi = (4 * dentro_circulo_total) / num_pontos  # Calcula a estimativa de Pi
    fim = time.time()  # Marca o fim da medição do tempo
    tempos.append(fim - inicio)  # Armazena o tempo de execução
    valores_pi.append(pi)  # Armazena o valor estimado de Pi
    print(f"Pi (Paralelo) com {num_pontos} amostras: {pi}")  # Imprime o valor estimado de Pi
    print(f"Tempo (Paralelo) com {num_pontos} amostras: {fim - inicio} segundos")  # Imprime o tempo de execução

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