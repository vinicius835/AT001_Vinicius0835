numeros = []
for i in range(10):
    try:
        #armazena o elemento digitado
        numero = int(input('Digite um número inteiro: '))
        numeros.append(numero)
    #Se o valor for incorreto
    except ValueError:
        print('Entrada inválida!!!')
    #Função SUM: soma automaticamente todos os numeros dentro dos elementos
soma = sum(numeros)
    #Calcula a média
media = soma / len(numeros)
print('Soma:', soma)
print('Média:', media)
