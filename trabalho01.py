from msilib import sequence
from msilib.schema import tables
import mysql.connector
 
mydb = mysql.connector.connect(
    host="relational.fit.cvut.cz",
    user="guest",
    password="relational",
    database="northwind"
)
 
mycursor = mydb.cursor()
 
def achar(tabela, coluna):
    if tabela == "tabela":
        mycursor.execute(f"SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA = 'northwind'")
    else:
        mycursor.execute(f"SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{coluna}' and table_schema = 'northwind';")
   
    myresult = mycursor.fetchall()
 
    enumerar = 1
 
    for elemento in myresult:
        print(f"{enumerar} - {elemento[0]}")
        enumerar += 1
 
    tabColEsc = input(f"Insira o código (número) da {tabela} que deseja fazer a procura: ")
 
    procurar = 1
 
    for elemento in myresult:
        if tabColEsc == str(procurar):
            tabColEsc = elemento[0]
            return tabColEsc
        procurar += 1
 
 
tabela = achar("tabela", "Vazio")
 
coluna = achar("coluna", tabela)
 
buscar = input(f"O que deseja achar em '{coluna}': ")
 
mycursor.execute(f"select * from `{tabela}` where `{coluna}` like '{busca}'")
 
myresult = mycursor.fetchall()

for elemento in myresult:
    print(elemento)
