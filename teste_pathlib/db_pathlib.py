import pathlib
from pathlib import Path

caminho_proj1 = Path()
caminho_proj2 = Path(__file__)

print(caminho_proj1.absolute)
print(caminho_proj2.absolute)
print(caminho_proj2)
print(caminho_proj2.parent)

novodir = caminho_proj2.parent / 'novodir'
print(novodir)

print(Path.home())

arquivo = caminho_proj2.parent / 'arq_teste.txt'
# Cria o arquivo
arquivo.touch()
print(arquivo)
# Escreve conteúdo no arquivo
# arquivo.write_text('Olá, esse é um exemplo!\n2 linha')
# print(arquivo.read_text())
# Exclui o arquivo
# arquivo.unlink()
arquivo.write_text('')

with arquivo.open('a+') as file:
    file.write('Primeira linha\n')
    file.write('Segunda linha\n')
    file.write('Terceira linha\n')

print(arquivo.read_text())

subpasta = arquivo.parent / 'subpasta'
subpasta.mkdir(exist_ok=True)
