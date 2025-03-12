import sqlite3

con = sqlite3.connect("vital_db.db")
cur = con.cursor()

# Consultar todos os registros
cur.execute("SELECT * FROM usuarios")
resultados = cur.fetchall()
for linha in resultados:
    print(linha)

# Consultar registros com filtros
cur.execute("SELECT * FROM usuarios WHERE idade > ?", (30,))
resultados = cur.fetchall()
print(resultados)
