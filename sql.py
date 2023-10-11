#kajakj hjaskjask

import sqlite3

def connection():
    conn = sqlite3.connect("Limpieza.db")
    cursor = conn.cursor()

    sql = """

    CREATE TABLE Fraud(
    id INTEGER PRIMARY KEY ,
    step INTEGER,
    type TEXT,
    amount REAL,
    nameOrig TEXT,
    oldbalanceOrg INTEGER,
    newbalanceOrig REAL,
    nameDest TEXT,
    oldbalanceDest INTEGER,
    newbalanceDest INTEGER,
    isFraud INTEGER,
    isFlaggedFraud INTEGER,
    ) 
    """

    cur.execute(sql)
    print("Base de datos creada wuwu")

    conn.commit()
    conn.close()


