import sqlite3

con = sqlite3.connect("vital_db.db")
cur = con.cursor()

# Inserindo um registro
cur.execute("""
INSERT INTO usuarios (nome, idade, email) 
VALUES (?, ?, ?)
""", ("João Silva", 30, "joao@gmail.com"))
con.commit()

# Inserindo múltiplos registros
usuarios = [
    ("Maria Souza", 25, "maria@gmail.com"),
    ("Carlos Lima", 40, "carlos@gmail.com")
]
cur.executemany("""
INSERT INTO usuarios (nome, idade, email) 
VALUES (?, ?, ?)
""", usuarios)
con.commit()
