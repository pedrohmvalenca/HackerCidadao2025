import sqlite3

# Conectando ao banco de dados (cria o arquivo se não existir)
con = sqlite3.connect("vital_db.db")

# Criar um cursor para executar comandos SQL
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    email TEXT UNIQUE
)
""")
con.commit()
