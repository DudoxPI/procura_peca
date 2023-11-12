import pandas as pd
import os

# Carregue o arquivo XLSX em um DataFrame
file_path = 'pecas.xlsx'
df = pd.read_excel(file_path)

while True:
    
    # Valor a ser procurado
    valor_procurado = input('Digite cod ou nome: ')
    os.system('cls')

    if valor_procurado == '':
        print('campo nao pode ficar em branco!')
        continue

    # Colunas onde você deseja procurar
    colunas_para_procurar = ['Código', 'Descrição', 'Observação']

    # Crie uma série booleana para cada coluna que corresponda ao valor procurado
    resultados = df[colunas_para_procurar].apply(lambda coluna: coluna.str.contains(valor_procurado, case=False, na=False))

    # Use o operador "any" para verificar se algum valor True foi encontrado em cada linha
    linhas_com_correspondencia = resultados.any(axis=1)

    # Exiba as linhas onde a correspondência foi encontrada
    correspondencias_encontradas = df[linhas_com_correspondencia]

    # Exiba o resultado
    if not correspondencias_encontradas.empty:
        print(correspondencias_encontradas)
    else:
        print('Nenhuma peça encontrada!')
