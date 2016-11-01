# Esse programa cria três arquivos com números inteiros aleatórios entre 1 e 10000
# Cada arquivo contém uma quantidade diferente de números
# arquivo1 = 1000 elementos
# arquivo2 = 100000 elementos
# arquivo3 = 1000000 elementos
# coding = utf-8

import random

def gerador_arquivo(filename, qtd):
    file = open(filename, "w")

    for i in range(qtd):
        numero = random.randint(1, 10000)
        file.write("{}".format(numero))
        if i % 100 == 0 and i != 0:
            file.write("\n")
        elif i != qtd-1:
            file.write(" ")
    
    file.close()


def main():
    gerador_arquivo("arquivo1.txt", 10)
    gerador_arquivo("arquivo2.txt", 100000)
    gerador_arquivo("arquivo3.txt", 1000000)

if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0))