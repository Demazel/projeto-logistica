import tkinter as tk
# tk inter é uma biblioteca de interface grafica para python
from tkinter import ttk
# o ttk são os widgets do python (coisas que posso interagir)
from funcoes import *

# vamos criar a nossa tela
root = tk.Tk()
# cria a tela principal do sistema
root.title("Projeto scrum - logistica")
# criar o tamango da tela ("largura x altura")
root.geometry("400x300")

# --- CABECALHO ---
cabecalho = ttk.Label(
    #  qual tela ele vai
    root,
    # Qual a informacao
    text = "Logistica Alpha",
    # qual fonte
    font = ("Arial", 20, "bold")    
)
# atribuir tela
cabecalho.pack(pady=20)
# --- FIM DO CABECALHO ---

# --- SUBTITULO ---
sub_titulo = ttk.Label(
    root,
    
    text = "Frete mais rápido é aqui",
    
    font = ("Arial", 12, "italic")
) 
sub_titulo.pack(pady=20)
# --- fim do subtitulo ---

# --- criar a area dos botoes (é tipo uma div do html) ----
tela_tbn = ttk.Frame(root)
# criei um espaço para os botões e coloquei na tela principal (root)
tela_tbn.pack(pady=20)

# --- criar os botões ---
btn_ver_frete = ttk.Button(tela_tbn, text = "Ver Fretes")
# ttk.Button (onde, texto)

btn_add_frete = tk.Button(tela_tbn, text="Adicionar Fretes", command=abrir_formulario_frete)

btn_ver_cliente = tk.Button(tela_tbn, text="Ver Clientes")

btn_add_cliente = tk.Button(tela_tbn, text="Adicionar Clientes", command=abrir_formulario_cliente)

# --- exibir os botoes ---
# para ver os botoes eu crio uma tabela e falo qual linha e qual coluna vai exibir
btn_ver_frete.grid(row=0, column=0, pady=10, padx=10)
btn_add_frete.grid(row=1, column=0, pady=10, padx=10)
btn_ver_cliente.grid(row=0, column=1, pady=10, padx=10)
btn_add_cliente.grid(row=1, column=1, pady=10, padx=10)

# para ver a tela
root.mainloop()