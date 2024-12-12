# Importação das bibliotecas utilizadas 
import serial as ard
import pandas as pd
import time


# Função que lê o valor relativo ao sensor pelo Serial
def read_data(temperatura, umidade):
    global arduino
    dados = arduino.readline().decode('utf-8').strip().split(',')
    dados_umidade = dados[0]
    dados_temperatura = dados[1]
    print(f"Dados recebidos: {dados_umidade}, {dados_temperatura}")
    umidade.append(dados_umidade)
    temperatura.append(dados_temperatura)


# Conecta ao serial pela porta utilizada pelo arduino
arduino = ard.Serial('COM11', 9600) # Alterar para o relativo ao seu computador

contador = 1 # contador para controlar o número de leituras
MAX_VALUE = 150 # número máximo de leituras dos dados
# listas que armazenarão os valores lidos, relativos para cada volume de água
lista_temperatura = []
lista_umidade = []

# Leitura de dados, com o volume de 50mL
while contador <= MAX_VALUE:    
    read_data(lista_temperatura, lista_umidade)
    contador += 1

# Cria o dataframe utilizando as listas, para que possamos analisar esses dados
df = pd.DataFrame({'Temperatura': lista_temperatura, 'Umidade': lista_umidade})
# Exporta para csv o arquivo gerado com os dados
df.to_csv('dados_arduino.csv', index=False)

print(df)