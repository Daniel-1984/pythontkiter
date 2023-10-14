# banco.py
import sqlite3 as lite

def connect_db():
    return lite.connect("dados.db")

def create_table():
    con = connect_db()
    try:
        with con:
            cur = con.cursor()
            cur.execute("""
                            CREATE TABLE IF NOT EXISTS clientes (
                            id INTEGER PRIMARY KEY,
                                nome TEXT,
                                email TEXT,
                                telefone TEXT,
                                data TEXT,
                                estado TEXT,
                                consulta TEXT
                                                    )
                                """)
            con.commit()
    except lite.Error as e:
        print("Erro no SQLite:", e)
    finally:
        con.close()

def insert_data(nome, email, telefone, data, estado, consulta):
    con = connect_db()
    try:
        with con:
            cur = con.cursor()
            cur.execute("INSERT INTO clientes (nome, email, telefone, data, estado, consulta) VALUES (?, ?, ?, ?, ?, ?)",
                        (nome, email, telefone, data, estado, consulta))
            con.commit()
    except lite.Error as e:
        print("Erro no SQLite:", e)
    finally:
        con.close()

def insert_data(nome, email, telefone, data, estado, consulta):
    con = connect_db()
    try:
        with con:
            cur = con.cursor()
            cur.execute("INSERT INTO clientes (nome, email, telefone, data, estado, consulta) VALUES (?, ?, ?, ?, ?, ?)",
                        (nome, email, telefone, data, estado, consulta))
            con.commit()
    except lite.Error as e:
        print("Erro no SQLite:", e)
    finally:
        con.close()

def fetch_all_data():
    con = connect_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM clientes")
    data = cur.fetchall()
    con.close()
    return data