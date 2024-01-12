import os
import pyaes

## abrir o arquivo criptografado
arq_nome = "teste.txt.ransomwaretroll"
arq = open(arq_nome, "rb")
arq_data = arq.read()
arq.close()

## chave para descriptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
dados_decriptados = aes.decrypt(arq_data)

## remover o arquivo criptografado
os.remove(arq_nome)

## criar o arquivo descriptografado
novo_arq = "teste.txt"
novo_arq = open(f'{novo_arq}', "wb")
novo_arq.write(dados_decriptados)
novo_arq.close()
