import tkinter as tk
import mysql.connector

def salvar():
    nome_mat = nome_mat_entry.get()
    nota = nota_entry.get()

    # Conectando ao banco de dados
    conn = mysql.connector.connect(
        host="host_do_banco_de_dados",
        user="usuario",
        password="senha",
        database="nome_do_banco_de_dados"
    )

    cursor = conn.cursor()

    # Inserindo os dados na tabela
    cursor.execute(f"INSERT INTO notas (nome_mat, nota) VALUES ('{nome_mat}', '{nota}')")
    conn.commit()

    cursor.close()
    conn.close()

def visualizar():
    # Conectando ao banco de dados
    conn = mysql.connector.connect(
        host="host_do_banco_de_dados",
        user="usuario",
        password="senha",
        database="nome_do_banco_de_dados"
    )

    cursor = conn.cursor()

    # Consultando os dados na tabela
    cursor.execute("SELECT * FROM notas")
    resultados = cursor.fetchall()

    # Exibindo os resultados na tela
    for resultado in resultados:
        id_, nome_mat, nota = resultado
        resultados_label = tk.Label(text=f"ID: {id_}, Nome da Matéria: {nome_mat}, Nota: {nota}")
        resultados_label.pack()

    cursor.close()
    conn.close()

app = tk.Tk()
app.title("Gerenciamento de Notas")

nome_mat_label = tk.Label(text="Nome da Matéria:")
nome_mat_label.pack()

nome_mat_entry = tk.Entry()
nome_mat_entry.pack()

nota_label = tk.Label(text="Nota:")
nota_label.pack()

nota_entry = tk.Entry()
nota_entry.pack()

salvar_button = tk.Button(text="Salvar", command=salvar)
salvar_button.pack()

visualizar_button = tk.Button(text="Visualizar", command=visualizar)
visualizar_button.pack()

app.mainloop()




