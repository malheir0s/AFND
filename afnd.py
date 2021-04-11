class Linguagem:

    def __init__(self):
        self.estados = []
        self.simbolos = []
        self.dicionario = dict()
        self.palavrasTeste = []
        self.estadosFinais = []
        self.pilhaTransicoes = []

    def lerTransicoes(self, num):
        for i in range (0, num):
            transicoes = input().split()
            self.criarDicionario(transicoes)

    def criarDicionario(self, transicoes):
        dupla = transicoes[0]+transicoes[1]
        if(dupla in self.dicionario):
            self.dicionario[dupla] = self.dicionario[dupla] + [transicoes[2]] 
        else:
            novaTransicao = {transicoes[0]+transicoes[1]:[transicoes[2]]}
            self.dicionario.update(novaTransicao)

    def validarTransicao(self, estado, simbolo):
        if((estado+simbolo) in self.dicionario):
            return self.dicionario.get(estado+simbolo)
        else:
            return False

    def percorrerPalavra(self, palavra, estadoInicial):
        self.pilhaTransicoes = [estadoInicial]
        for caractere in palavra:
            novaPilha = []
            for estados in self.pilhaTransicoes:
                estadosFuturos = self.validarTransicao(estados, caractere)
                if(estadosFuturos):
                    for estado in estadosFuturos:
                        novaPilha.append(estado)
            self.pilhaTransicoes = novaPilha


        aceita = False
        for estado in self.pilhaTransicoes:
            if(estado in self.estadosFinais):
                aceita = True
                break
    
        if(aceita):
            print('S')
        else:
            print('N')
            


L1 = Linguagem()
L1.estados = input()
L1.simbolos = input()
numeroTransicoes = int(input())
L1.lerTransicoes(numeroTransicoes)
estadoInicial = input()
L1.estadosFinais = input().split()
L1.palavrasTeste = input().split()

for words in L1.palavrasTeste:
    L1.percorrerPalavra(words, estadoInicial)


