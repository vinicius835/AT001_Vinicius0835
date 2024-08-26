def obter_ultimo_elemento(lista):
    #se for o ultimo numero, este numera será armazenado
    if lista:
        return lista[-1]
    #Senão, é ignorado
    else: return None
lista=list()
i=1
while i<=5:
    elem = int(input('Digite um elemento da lista:'))
    lista.append(elem)
    i+=1
    print(lista)
    ultimo_elemento = obter_ultimo_elemento(lista)
print('Último elemento da lista:', ultimo_elemento)