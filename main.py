import Tabella

tipo_attacco = input("Insert attacking type: ")
tipo_difesa= input("Insert defence type: ")

try:
    print(Tabella.get_move_result(tipo_attacco.lower(),tipo_difesa.lower()))
except:
    print("Error, please retype")