import csv
import os
# os é as funções do sistema operacional (operational sistem)

dados_frete = "dados_frete.csv"
dados_cliente = "dados_cliente.csv"
# dizendo o nome do arquivo

campo_fretes = ["registro_frete","origem,destino","cliente","produto","status"]
campos_cliente = ["registro_cliente","nome","sobrenome","cidade","bairro"]
# informar os campos do frete

# funções

# adicionar_registros_frete  - segurança pro sistema
# abrir_o_formulado do frete
# salvar_o_frete
import tkinter as tk


def abrir_formulario_frete():
    popup_frete = tk.Toplevel()
    popup_frete.title("Adicionar Fretes")
    popup_frete.geometry("500x500")
    
    labels_fretes = ["registro_frete","origem,destino","cliente","produto","status"]
    fretes = {}
    
    # vou sequenciar campo com dados
    for campo_dados in labels_fretes:
        # para cada campo que o usuario digita
        tk.Label(popup_frete, text = campo_dados).pack(pady=5)
        # essa linha cria todos os textos para o usuario 
        entrada_fretes = tk.Entry(popup_frete)
        # entry (caixa de texto)
        entrada_fretes.pack()
        fretes[campo_dados] = entrada_fretes
    
    def salvar():
        dados = {campo_dados:fretes[campo_dados].get() for campo_dados in fretes}
        add_fretes(dados)
        # fechar automatico uma janela
        popup_frete.destroy()
            
    tk.Button(popup_frete, text = "SALVAR", command = salvar).pack(pady=5)
    tk.Button(popup_frete, text = "LIMPAR", pady=5).pack()

def add_fretes(registro):
    # para manipular o arquivo
    arquivo = os.path.isfile(dados_frete)
    
    # add valores
    # sempre que usamos o with open informamos
    # 1 - arquivo, 2 - modo, 3 - novas linhas, 4 - utf-8
    
    with open(dados_frete, "a", newline="", encoding="utf-8") as arquivo_fretes:
        escrever = csv.DictWriter(arquivo_fretes, fieldnames=campo_fretes, delimiter=";")
        
        # para adicionar os dados no csv
        escrever.writerow(registro)


# -------------------------- Formulario cliente

 
def abrir_formulario_cliente():
    popup_cliente = tk.Toplevel()
    popup_cliente.title("Adicionar Clientes")
    popup_cliente.geometry("500x500")
    
    labels_cliente = ["registro_cliente","nome","sobrenome","cidade","bairro"]
    cliente = {}
    
    for campos_cliente in labels_cliente:
        tk.Label(popup_cliente, text = campos_cliente).pack(pady=5)
        entrada_cliente = tk.Entry(popup_cliente)
        entrada_cliente.pack()
        cliente[campos_cliente] = entrada_cliente
        
    def salvar_clientes():
        data_cliente = {campos_cliente:cliente[campos_cliente].get() for campos_cliente in cliente}
        add_cliente(data_cliente)
        popup_cliente.destroy()
        
    tk.Button(popup_cliente, text = "SALVAR", command= salvar_clientes).pack(pady=5)
    tk.Button(popup_cliente, text = "LIMPAR", pady=5).pack()
    
def add_cliente(reg_client):
    arquivo_cliente = os.path.isfile(dados_cliente)
    
    with open(dados_cliente, "a", newline="", encoding="utf8") as arquivo_clientes:
        write_clientes = csv.DictWriter(arquivo_clientes, fieldnames = campos_cliente, delimiter=";")
        write_clientes.writerow(reg_client)