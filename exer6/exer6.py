def converter_quilometros_para_metros(quilometros):
    #Converte quilometros em metros
    metros = quilometros * 1000 
    return metros 
try:
    quilometros = float(input('Digite a distância em quilômetros: ')) 
    metros = converter_quilometros_para_metros(quilometros)
    print('metros:', metros) 
    #Será mando em except se estiver algum erro
except ValueError: 
    print('Entrada inválida!')