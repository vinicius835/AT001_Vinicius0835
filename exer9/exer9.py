def insertion_sort(lista): 
    #ordena os numeros digitados
    for i in range(len(lista)): 
        chave = lista[i]
        j = i - 1 
        while j >= 0 and chave < lista[j]: 
            lista[j + 1] = lista[j]
            j-= 1
            lista[j + 1] = chave 
#Comando list(), ela faz a lista se tornar uma lista
lista = list()
i=1 
while i<=10: 
    elem = int(input('Digite um elemento da lista:'))
    lista.append(elem) 
    i+=1 
    print(lista) 
    insertion_sort(lista) 
    print(lista)