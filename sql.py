#kajakj hjaskjask

import sqlite3
conn = sqlite3.connect("Limpieza.db")
cur = conn.cursor()

sql = """

CREATE TABLE Fraud(
    Id_Step INTEGER,
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
    primary key(Id_Step)

    ) """

    cur.execute(sql)
    print("Base de datos creada wuwu")

    conn.commit()
    conn.close()
