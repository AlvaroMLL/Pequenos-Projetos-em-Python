'''

-------------------------------------------------------------
EXERCÍCIO: Torres de Hanói
-------------------------------------------------------------
DESCRIÇÃO DO PROBLEMA:
O Problema das Torres de Hanói é um clássico da computação e da matemática.
Consiste em três pinos e um conjunto de discos de tamanhos diferentes, empilhados
em ordem crescente de diâmetro (do menor no topo ao maior na base) em um dos pinos.

O objetivo é mover todos os discos para outro pino qualquer, utilizando um pino auxiliar,
seguindo as seguintes regras:
1. Apenas um disco pode ser movido por vez.
2. Um disco maior nunca pode ser colocado sobre um disco menor.
3. Todos os discos devem ser movidos respeitando as regras acima.
-------------------------------------------------------------

'''

#Início

class Pilha:
    def __init__(self):
        self.__itens = []

    def vazia(self):
        return len(self.__itens) == 0
    
    def empilhar(self, dado):
        self.__itens.append(dado)
    
    def desempilhar(self):
        if(self.vazia()):
            return None
        return self.__itens.pop()
        
    def elem_topo(self):
        if(self.vazia()):
            return None
        return self.__itens[-1]        
    
    def exibir_pilha(self):
        print('Pilha:', end=' ')
        if self.vazia():
            print('vazia')
        else:
            for dado in self.__itens:
                print(dado, end=' ')
            print()
    
    def tamanho_pilha(self):
        len(self.__itens)
    
    def copiar(self):
        return self.__itens.copy()

#Programa Principal 

p1 = Pilha()
p2 = Pilha()
p3 = Pilha()


while True:
        qtd_discos = int(input('Quantidade de discos: '))
        if qtd_discos % 2 == 0 or qtd_discos == 2:
                print('Só números impares')
        else:
            for i in range(qtd_discos):
                p1.empilhar(qtd_discos - i)
            break


    
p1.exibir_pilha

while True:
    sequencia_certa = [i for i in range(qtd_discos, 0, -1)]
    print('TORRE DE HANOI')
    print('[1] TROCAR DISCO DE PILHA')
    print('[2] SAIR')
    op = input("DIGITE SUA OPÇÃO: ")
    if op == '1':
        p1.exibir_pilha()
        p2.exibir_pilha()
        p3.exibir_pilha()
        op2 = input('DE QUAL PILHA: ')
        if op2 == '1':
            dado = p1.elem_topo()
            op3 = input('PARA QUAL PILHA: ')
            if op3 == '2':
                if p2.elem_topo() == None:
                    dado = p1.desempilhar()
                    p2.empilhar(dado)
                elif dado > p2.elem_topo():
                    print('Um disco maior nunca pode ser colocado sobre um disco menor')
                else:
                    dado = p1.desempilhar()
                    p2.empilhar(dado)
            if op3 == '3':
                if p3.elem_topo() == None:
                    dado = p1.desempilhar()
                    p3.empilhar(dado)
                elif dado > p3.elem_topo():
                    print('Um disco maior nunca pode ser colocado sobre um disco menor')
                else:
                    dado = p1.desempilhar()
                    p3.empilhar(dado)
        if op2 == '2':
            dado = p2.elem_topo()
            op3 = input('PARA QUAL PILHA: ')
            if op3 == '1':
                if p1.elem_topo() == None:
                    dado = p2.desempilhar()
                    p1.empilhar(dado)
                elif dado > p1.elem_topo():
                    print('Um disco maior nunca pode ser colocado sobre um disco menor')
                else:
                    dado = p2.desempilhar()
                    p1.empilhar(dado)
            if op3 == '3':
                if p3.elem_topo() == None:
                    dado = p2.desempilhar()
                    p3.empilhar(dado)
                elif dado > p3.elem_topo():
                    print('Um disco maior nunca pode ser colocado sobre um disco menor')
                else:
                    dado = p2.desempilhar()
                    p3.empilhar(dado)
        if op2 == '3':
            dado = p3.elem_topo()
            op3 = input('PARA QUAL PILHA: ')
            if op3 == '1':
                if p1.elem_topo() == None:
                    dado = p3.desempilhar()
                    p1.empilhar(dado)
                elif dado > p1.elem_topo():
                    print('Um disco maior nunca pode ser colocado sobre um disco menor')
                else:
                    dado = p3.desempilhar()
                    p1.empilhar(dado)
            if op3 == '2':
                if p2.elem_topo() == None:
                    dado = p3.desempilhar()
                    p2.empilhar(dado)
                elif dado > p2.elem_topo():
                    print('Um disco maior nunca pode ser colocado sobre um disco menor')
                else:
                    dado = p3.desempilhar()
                    p2.empilhar(dado)
    if (p1.copiar() == sequencia_certa or p2.copiar() == sequencia_certa or p3.copiar() == sequencia_certa):
        print('\n🎉 VOCÊ GANHOU!!! TODOS OS DISCOS FORAM MOVIDOS COM SUCESSO!\n')
        break
    if op == '2':
        break


    
    