import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Instruções para instalar os módulos necessários:
# 1. Instale o Python no Windows 10 a partir do site oficial: https://www.python.org
# 2. Certifique-se de que o MySQL está instalado e configurado no seu sistema.
# 3. Instale os módulos necessários com os seguintes comandos no terminal:
#    pip install mysql-connector-python

# Configuração do banco de dados MySQL
def configurar_base_dados():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sua_senha"  # Substitua pela sua senha
        )
        cursor = conexao.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS convidados_db")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS convidados_db.convidados (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255),
                palavra_passe VARCHAR(255),
                email VARCHAR(255),
                telefone VARCHAR(15)
            )
        """)
        conexao.commit()
        conexao.close()
    except mysql.connector.Error as e:
        messagebox.showerror("Erro na Base de Dados", f"Erro: {str(e)}")

# Função para adicionar um convidado
def adicionar_convidado():
    nome = entrada_nome.get()
    palavra_passe = entrada_palavra_passe.get()
    email = entrada_email.get()
    telefone = entrada_telefone.get()
    
    if not nome or not palavra_passe or not email or not telefone:
        messagebox.showwarning("Campos Vazios", "Todos os campos são obrigatórios!")
        return

    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sua_senha",  # Substitua pela sua senha
            database="convidados_db"
        )
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO convidados (nome, palavra_passe, email, telefone)
            VALUES (%s, %s, %s, %s)
        """, (nome, palavra_passe, email, telefone))
        conexao.commit()
        conexao.close()
        listar_convidados()
        limpar_campos()
        messagebox.showinfo("Sucesso", "Convidado adicionado com sucesso!")
    except mysql.connector.Error as e:
        messagebox.showerror("Erro", f"Erro ao adicionar convidado: {str(e)}")

# Função para remover um convidado
def remover_convidado():
    selecionado = lista_convidados.curselection()
    if not selecionado:
        messagebox.showwarning("Nenhum Selecionado", "Selecione um convidado para remover.")
        return

    try:
        convidado = lista_convidados.get(selecionado)
        convidado_id = convidado.split(" - ")[0]  # Assumindo que o ID é a primeira parte
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sua_senha",  # Substitua pela sua senha
            database="convidados_db"
        )
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM convidados WHERE id = %s", (convidado_id,))
        conexao.commit()
        conexao.close()
        listar_convidados()
        messagebox.showinfo("Sucesso", "Convidado removido com sucesso!")
    except mysql.connector.Error as e:
        messagebox.showerror("Erro", f"Erro ao remover convidado: {str(e)}")

# Função para listar os convidados
def listar_convidados():
    lista_convidados.delete(0, tk.END)
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sua_senha",  # Substitua pela sua senha
            database="convidados_db"
        )
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, email FROM convidados")
        for convidado in cursor.fetchall():
            lista_convidados.insert(tk.END, f"{convidado[0]} - {convidado[1]} ({convidado[2]})")
        conexao.close()
    except mysql.connector.Error as e:
        messagebox.showerror("Erro", f"Erro ao listar convidados: {str(e)}")

# Função para limpar os campos de entrada
def limpar_campos():
    entrada_nome.delete(0, tk.END)
    entrada_palavra_passe.delete(0, tk.END)
    entrada_email.delete(0, tk.END)
    entrada_telefone.delete(0, tk.END)

# Configuração da interface gráfica
configurar_base_dados()
janela = tk.Tk()
janela.title("Lista de Convidados")
janela.geometry("600x400")

# Labels e entradas
tk.Label(janela, text="Nome:").pack()
entrada_nome = tk.Entry(janela)
entrada_nome.pack()

tk.Label(janela, text="Palavra-passe:").pack()
entrada_palavra_passe = tk.Entry(janela, show="*")
entrada_palavra_passe.pack()

tk.Label(janela, text="E-mail:").pack()
entrada_email = tk.Entry(janela)
entrada_email.pack()

tk.Label(janela, text="Telefone:").pack()
entrada_telefone = tk.Entry(janela)
entrada_telefone.pack()

# Botões
tk.Button(janela, text="Adicionar", command=adicionar_convidado).pack(pady=5)
tk.Button(janela, text="Remover", command=remover_convidado).pack(pady=5)

# Lista de convidados
lista_convidados = tk.Listbox(janela, width=50, height=10)
lista_convidados.pack()

# Inicializar a lista de convidados
listar_convidados()

# Iniciar a aplicação
janela.mainloop()
