def maior3(a, b, c):
    # se o valor A for maior que o valor B e C, o valor A será o valor mostrado em 'resultado'
    if a >= b and a >= c: 
        return a 
    #se o valor B for maior que o valor A e C, o valor B será o valor mostrado em 'resultado'
    elif b >= c: 
        return b
    #se o valor C for maior que o valor A e B, o valor C será o valor mostrado em 'resultado'
    else: return c
n1=int(input('Digite um número:')) 
n2=int(input('Digite um número:')) 
n3=int(input('Digite um número:')) 
resultado = maior3(n1,n2,n3) 
print(resultado)