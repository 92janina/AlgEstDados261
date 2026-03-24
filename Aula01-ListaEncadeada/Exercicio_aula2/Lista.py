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
            aux = self.inicio
            while aux.prox is not None and aux.prox.dado < valor:
                aux = aux.prox
            nodo.prox = aux.prox
            aux.prox = nodo
        self.imprimir()
      



