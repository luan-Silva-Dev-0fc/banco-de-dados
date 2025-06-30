# Projeto de Banco de Dados com Python e SQLite

## ✅ VISÃO GERAL

Este projeto utiliza **Python** e **SQLite** para criar um banco de dados simples que armazena informações sobre usuários. O banco de dados é salvo em um arquivo `.db` e a interação com o banco é feita através de scripts Python executados no terminal (CMD).

### 📌 Ferramentas Utilizadas:

- **Python**: Linguagem de programação para criar o banco de dados e manipular os dados.
- **SQLite**: Banco de dados leve que salva tudo em um arquivo `.db`.
- **CMD (Terminal)**: Onde os scripts foram executados.
- **Bloco de Notas**: Editor de texto simples usado para escrever o código Python.

---

## 🧱 O QUE FOI CRIADO

### 🗃️ 1. Banco de Dados
O banco de dados é chamado `meubanco.db` e é criado ou acessado com o seguinte código:

```python
conexao = sqlite3.connect("meubanco.db")
🧱 2. Tabela
Dentro do banco de dados, foi criada uma tabela chamada usuarios com 3 colunas:

id: Chave primária que é gerada automaticamente.

nome: Texto obrigatório.

idade: Número inteiro.

python
Copiar
Editar
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER
)
""")
✍️ 3. Inserção de Dados no Código Fixo
O primeiro exemplo insere um usuário com nome "Luan" e idade 25 diretamente no código:

python
Copiar
Editar
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", ("Luan", 25))
⌨️ 4. Inserção Via Terminal (Input)
O código também permite inserir dados no banco através do terminal, pedindo o nome e a idade do usuário:

python
Copiar
Editar
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", (nome, idade))
📋 5. Visualizar os Dados Salvos
O script a seguir lê e exibe os dados salvos no banco:

python
Copiar
Editar
cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()

for usuario in usuarios:
    print(usuario)
📂 ARQUIVOS DO PROJETO
Nome do Arquivo	Função
banco.py	Cria o banco de dados e a tabela, insere um usuário fixo.
inserir_dados.py	Pede nome e idade no terminal e salva os dados.
ver_dados.py	Lê e exibe os dados salvos no banco.
meubanco.db	Arquivo onde os dados são armazenados (banco de dados).

🔁 CICLO COMPLETO
Criação do banco de dados SQLite.

Criação da tabela para armazenar informações dos usuários.

Inserção de dados (fixos e através do terminal).

Leitura dos dados salvos e exibição no terminal.

🔐 Segurança (extra)
O SQLite não tem controle de senha por padrão e é ideal para projetos pequenos e locais. Não é recomendado para projetos de alta escala ou com muitos acessos simultâneos.

🧠 O QUE FOI APRENDIDO
Você aprendeu a:

Conceito	Já aprendeu? ✅
Criar banco	✅
Criar tabela	✅
Inserir dados	✅
Ler dados	✅
Usar input no terminal	✅
Ver dados no .db	✅

