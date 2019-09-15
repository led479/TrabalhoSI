from classes.estado import Estado
while(True):
    e = Estado()
    print(e.matriz[0])
    print(e.matriz[1])
    print(e.matriz[2])
    print(e.indice_do_vazio())

    for filhos in e.filhos():
        print("-------FILHO-------")
        print(filhos[0])
        print(filhos[1])
        print(filhos[2])