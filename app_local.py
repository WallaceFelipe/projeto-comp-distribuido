# Essa aplicação tem o intuito de rodar localmente
# ela lerá o arquivo e irá fazer uma captura dos número que são primos (map)
# após esse agrupamento ele irá **reduzir** esse conjunto de de dados, mostrando apenas os que são diferentes

import  sys

def mapping(filename):
    file = open(filename, "r")
    primos = []
    while True:
        lista = file.readline()

        if lista == "":
            break

        for x in lista.split(" "):
            if x != "\n":
                x = int(x)
                ehprimo = False #aqui parte do principio que o numero não é primo

                if x == 2:
                    ehprimo = True
                
                if not (x % 2 == 0 or x == 1):
                    ehprimo = True       # aqui, por não ser um numero par, ele passa a considerar que o numero pode ser primo
                    for i in range(3, x//2, 2):
                        if x % i == 0:
                            ehprimo = False   # se ele avaliar que é divisível por algum numero, ele simplesmente afirma que não é primo
                
                if ehprimo:
                    if not x in primos:
                        primos.append(x)
    
    return primos


def main():
    lista = mapping("arquivo3.txt")
    print(lista)

if __name__ == '__main__':
    sys.exit(int(main() or 0))
        
