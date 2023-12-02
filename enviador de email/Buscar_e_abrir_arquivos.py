import os
import tkinter as tk
from tkinter import filedialog

def procurar_arquivo():
    nome_arquivo = entry_nome_arquivo.get()
    diretorio_procura = r"C:\\Users\\mocob\\Desktop"  # Substitua pelo caminho correto
    
    resultados = []
    
    for root, dirs, files in os.walk(diretorio_procura):
        for arquivo in files:
            if nome_arquivo in arquivo:
                caminho_completo = os.path.join(root, arquivo)
                resultados.append(caminho_completo)
    
    if resultados:
        label_resultado.config(text="Arquivos encontrados:")
        listbox_resultado.delete(0, tk.END)  # Limpa a lista atual
        for resultado in resultados:
            listbox_resultado.insert(tk.END, resultado)
        botao_abrir.config(state=tk.NORMAL)
    else:
        label_resultado.config(text=f'O arquivo {nome_arquivo} não foi encontrado.')
        botao_abrir.config(state=tk.DISABLED)

def abrir_arquivo():
    selecionado = listbox_resultado.get(listbox_resultado.curselection())
    os.startfile(selecionado)

# Configuração da janela principal
janela = tk.Tk()
janela.title("Procurar e Abrir Arquivo")

# Criação de widgets
label_instrucao = tk.Label(janela, text="Digite o nome do arquivo que deseja procurar:")
entry_nome_arquivo = tk.Entry(janela)
botao_procurar = tk.Button(janela, text="Procurar", command=procurar_arquivo)
label_resultado = tk.Label(janela, text="")
listbox_resultado = tk.Listbox(janela, width=100, height=20)  # Ajuste a largura e altura desejadas
botao_abrir = tk.Button(janela, text="Abrir Arquivo", command=abrir_arquivo, state=tk.DISABLED)

# Layout dos widgets
label_instrucao.pack()
entry_nome_arquivo.pack()
botao_procurar.pack()
label_resultado.pack()
listbox_resultado.pack()
botao_abrir.pack()

# Executa a interface gráfica
janela.mainloop()
