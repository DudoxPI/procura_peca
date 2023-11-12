import tkinter as tk
import pandas as pd

def pesquisar(event=None):
    valor_procurado = entrada_busca.get()
    resultado_text.delete(1.0, tk.END) #limpa a tela a cada resultado

    if valor_procurado == '':
        resultado_text.insert(tk.END, '*** Campo nâo pode ser vazio!')
        return

    colunas_para_procurar = ['CÓDIGO', 'DESCRIÇÃO', 'OBSERVAÇÃO']
    resultados = df[colunas_para_procurar].apply(lambda coluna: coluna.str.contains(valor_procurado, case=False, na=False))
    
    linhas_com_correspondencia = resultados.any(axis=1)
    correspondencias_encontradas = df[linhas_com_correspondencia].reset_index(drop=True )

    if not correspondencias_encontradas.empty:
        resultado_text.insert(tk.END, correspondencias_encontradas)
    else:
        resultado_text.insert(tk.END, f'*** Nenhuma peça encontrada!')
                              

# Carregue o arquivo XLSX em um DataFrame
file_path = 'pecas.xlsx'
df = pd.read_excel(file_path)


root = tk.Tk()
root.title('Pesquisa de Peças')
root.geometry('1024x400')

frame_busca = tk.Frame(root)
frame_busca.pack(pady=10)

label_busca = tk.Label(frame_busca, text='Buscar peças: ')
label_busca.pack(pady=10, side=tk.LEFT)

entrada_busca = tk.Entry(frame_busca, width=40)
entrada_busca.pack(side=tk.LEFT, padx=10)
entrada_busca.bind('<Return>', pesquisar)

botao_pesquisar = tk.Button(frame_busca, text='Buscar', command=pesquisar)
botao_pesquisar.pack(side=tk.LEFT)

resultado_text = tk.Text(root, wrap=tk.WORD)
resultado_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

root.mainloop()

    
