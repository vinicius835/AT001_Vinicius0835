def maior_menor(lista):
    maior = lista[0]
    menor = lista[0] 
    for elemento in lista:
        #Se o numero for maior que o numero habitado, ele vai se tornar o maior
        if elemento > maior:
            maior = elemento
            #Se o numero for menor que o numero habitado, ele vai se tornar o menor
        elif elemento < menor:
            menor = elemento
    return maior, menor
lista=list()
i=1 
#enquanto o i for menor do que 10 ele vai mostrar os numeros digitados
while i<=10: 
    elem = int(input('Digite um elemento da lista:')) 
    lista.append(elem)
    i+=1
    print(lista) 
maior, menor = maior_menor(lista) 
print('Maior:', maior) 
print('Menor:', menor)