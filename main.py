from PyQt5 import uic, QtWidgets
import sqlite3

app = QtWidgets.QApplication([])
tela_principal = uic.loadUi("./assets/layouts/untitled.ui")
conexao = sqlite3.connect("./assets/database/db.db")
cursor=conexao.cursor()
status_terminado='Concluido'
status_nao_terminado='Não Concluído'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tarefas(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               tarefa TEXT NOT NULL,
               status TEXT ,
               prioridade TEXT
)
''')



'''FUNÇÕES'''
def cadastrar_tarefa():
    tarefa_add = tela_principal.lineEdit.text()
    prioridade = "alta"
    cursor.execute(f'INSERT INTO tarefas (tarefa ,status, prioridade) VALUES ("{tarefa_add}", "{status_nao_terminado}", "{prioridade}")  ')
    conexao.commit()
    tela_principal.lineEdit.clear()
    listar_dados()
    

    

def atualizar_status_tarefa():
    listar_dados()


def listar_dados():
    cursor.execute("SELECT tarefa, status, prioridade FROM tarefas")
    dados_lidos = cursor.fetchall()
    tela_principal.tableWidget_3.setRowCount(len(dados_lidos))
    tela_principal.tableWidget_3.setColumnCount(3)
    teste='ola'
    for i in range(0, len(dados_lidos)):
        for j in range(0, 3):
            tela_principal.tableWidget_3.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

listar_dados()
'''CHAMADAS'''
tela_principal.pushButton.clicked.connect(cadastrar_tarefa)
tela_principal.refresh.clicked.connect(atualizar_status_tarefa)



tela_principal.show()
app.exec()

