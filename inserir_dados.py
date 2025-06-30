import sqlite3

nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))

conexao = sqlite3.connect("meubanco.db")
cursor = conexao.cursor()

cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", (nome, idade))

conexao.commit()
conexao.close()

print("Usuário salvo com sucesso!")
