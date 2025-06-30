import sqlite3

conexao = sqlite3.connect("meubanco.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER
)
""")

cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", ("Luan", 25))

conexao.commit()
conexao.close()
