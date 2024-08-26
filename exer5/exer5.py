def mdc(a, b):
    #calcula se o valor de b for igual a 0
    if b == 0: 
        return a 
    #calcula o mdc
    else: 
        return mdc(b, a % b) 
num1 = int(input('Digite um número:'))
num2 = int(input('Digite outro número:')) 
resultado = mdc(num1, num2)
print('MDC:', resultado)