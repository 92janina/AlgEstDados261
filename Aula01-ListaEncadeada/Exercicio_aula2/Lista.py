from No import No
#defino a estrutura da classe-aqui a lista em orde de chegada
class Lista:

    def __init__(self):
        self.inicio = None
    
    def imprimir(self):
        print("-----------------------------")
        print("Lista Encadeada por ordem de Crescente")
        if self.inicio is None:
            print("Lista Vazia")
        else:
            aux = self.inicio
            while aux:
                print( aux.dado )
                aux = aux.prox
#método
    def add(self,valor):
        nodo = No(valor)  # nodo-instancia do No-retorna referencia de memoria
        if self.inicio is None or valor < self.inicio.dado:
            self.inicio = nodo
        else:
            if nodo.dado < self.inicio.dado:
                nodo.prox = self.inicio
                self.inicio = nodo
            else:
                ant = self.inicio
                aux = self.inicio.prox
                while aux:
                    if nodo.dado < aux.dado:
                        nodo.prox = aux
                        ant.prox = nodo
                        break
                    else:
                        ant = aux 
                        aux = aux.prox
                if aux == None:
                    ant.prox = nodo        
        self.imprimir()                
            #aux = self.inicio
            #while aux.prox is not None and aux.prox.dado < valor:
                #aux = aux.prox
            #nodo.prox = aux.prox
            #aux.prox = nodo
        #self.imprimir()
    
    def remover(self, valor):
        if self.inicio == None:
            print("Lista vazia")
        else:
            removeu = False
            if valor == self.inicio.dado:
                self.inicio = self.inicio.prox
                removeu = True
            else:
                ant = self.inicio
                aux = self.inicio.prox
                while aux:
                    if valor == aux.dado:
                        ant.prox = aux.prox
                        removeu = True
                        break
                    else: 
                        ant = aux
                        aux = aux.prox
            if removeu:
                print(valor, "removido!")
            else:
                print(valor, "não encontrado!")
            self.imprimir()        



      



