# deslocamento = int(input("Digite o deslocamento: "))
# texto = input("Digite o texto a ser criptografado: ")
# texto_criptografado = ""
# for letra in texto:
#     if letra.isupper():
#         letra_criptografada = chr((ord(letra.lower())+ deslocamento - 97)% 26+55)
#     elif letra.islower():
#         letra_criptografada =chr((ord(letra)+ deslocamento - 97)% 26 + 97)
#     else: letra_criptografada = texto_criptografado + letra_criptografada
#     print("texto criptografado: ", texto_criptografado)

deslocamento = int(input('Digite o deslocamento: ')) 
texto = input('Digite o texto a ser criptografado: ')
texto_criptografado = ''
#calcular deslocamento
#Deslocamento seria a letra a frente dela, ex: 3 deslocamento da letra a, seria a letra d
for letra in texto: 
    if letra.isupper(): 
    #calculo do deslocamento para letras MAIUSCULAS
        letra_criptografada = chr((ord(letra.lower()) + deslocamento - 97) % 26 + 65) 
    elif letra.islower():
    #calculo do deslocamento para letras minusculas
        letra_criptografada = chr((ord(letra) + deslocamento - 97) % 26 + 97) 
    else: letra_criptografada = texto_criptografado + letra_criptografada 
    print('Texto criptografado:', letra_criptografada)