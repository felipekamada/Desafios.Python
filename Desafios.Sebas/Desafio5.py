def posicaomenor (lista):
    posicao = None
    for i in range(len(lista)):
        if (posicao is None):
            posicao = i
        elif lista[i] < lista[posicao]:
            posicao = i
    return posicao

