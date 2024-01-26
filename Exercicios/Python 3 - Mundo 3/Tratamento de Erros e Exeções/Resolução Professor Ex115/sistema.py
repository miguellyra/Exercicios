from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt' 

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas','Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq,nome,idade)
    elif resposta == 3:
        cabeçalho('Saindo do sitema... Até logo!')
        break
    else:
        print('ERRO! Digite uma opção válida!')
    sleep(2)

