import Database.database as db
import models.cliente as cliente
import logging

logging.basicConfig( level=logging.ERROR ,filename="Docs\app.log", format="% (asctime)s - %(levelname)s - %(message)s")

def Incluir(cliente):
    print("Incluindo...")
    try:
        count = db.cursor.execute("""
        INSERT INTO Cliente (cliNome, cliIdade, cliProfissao) 
        VALUES (?,?,?)""",
        cliente.nome, cliente.idade, cliente.profissao).rowcount
        db.cnxn.commit()
    except Exception:
        logging.exception(Exception)

def Alterar(cliente):
    print("alterando...")
    try:
        count = db.cursor.execute("""
        UPDATE Cliente
        SET cliNome = ?, cliIdade = ?, cliProfissao = ?
        WHERE id = ?
        """,
        cliente.nome, cliente.idade, cliente.profissao, cliente.id).rowcount
        db.cnxn.commit()
    except Exception:
        logging.exception(Exception)

def Excluir(id):
    print("Excluindo...")
    try:
        count = db.cursor.execute("""
        DELETE FROM Cliente WHERE id = ?""",
        id).rowcount
        db.cnxn.commit()
    except Exception:
        logging.exception(Exception)

def selecionarById(id):
    print("GetID...")
    try:
        db.cursor.execute("SELECT * FROM Cliente WHERE id = ?", id)
        costumerlist = []

        for row in db.cursor.fetchall():
            costumerlist.append(cliente.Cliente(row[0], row[1], row[2], row[3]))
        
        return costumerlist[0]
    except Exception:
        logging.exception(Exception)

def selecionartodos():
    print("GetAll...")
    try:
        db.cursor.execute("SELECT * FROM Cliente")
        costumerlist = []

        for row in db.cursor.fetchall():
            costumerlist.append(cliente.Cliente(row[0], row[1], row[2], row[3]))
        
        return costumerlist
    except Exception:
        logging.exception(Exception)