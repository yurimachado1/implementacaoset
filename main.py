class SetTabelaHash:
    def __init__(self):
        self.elementos = {}

    def adicionar(self, elemento):
        self.elementos[elemento] = True

    def remover(self, elemento):
        if elemento in self.elementos:
            del self.elementos[elemento]

    def contem(self, elemento):
        return elemento in self.elementos

    def tamanho(self):
        return len(self.elementos)

    def uniao(self, outro_conjunto):
        novo_conjunto = SetTabelaHash()
        novo_conjunto.elementos.update(self.elementos)
        novo_conjunto.elementos.update(outro_conjunto.elementos)
        return novo_conjunto

    def intersecao(self, outro_conjunto):
        novo_conjunto = SetTabelaHash()
        for elemento in self.elementos:
            if elemento in outro_conjunto.elementos:
                novo_conjunto.adicionar(elemento)
        return novo_conjunto

    def diferenca(self, outro_conjunto):
        novo_conjunto = SetTabelaHash()
        for elemento in self.elementos:
            if elemento not in outro_conjunto.elementos:
                novo_conjunto.adicionar(elemento)
        return novo_conjunto

    def __str__(self):
        return str(list(self.elementos.keys()))

# Exemplo de uso:
conjunto1 = SetTabelaHash()
conjunto1.adicionar(1)
conjunto1.adicionar(2)
conjunto1.adicionar(3)

conjunto2 = SetTabelaHash()
conjunto2.adicionar(2)
conjunto2.adicionar(3)
conjunto2.adicionar(4)

print("Conjunto 1:", conjunto1)
print("Conjunto 2:", conjunto2)

# União de conjuntos
resultado_uniao = conjunto1.uniao(conjunto2)
print("União de conjuntos:", resultado_uniao)

# Interseção de conjuntos
resultado_intersecao = conjunto1.intersecao(conjunto2)
print("Interseção de conjuntos:", resultado_intersecao)

# Diferença entre conjuntos
resultado_diferenca = conjunto1.diferenca(conjunto2)
print("Diferença entre conjuntos (conjunto1 - conjunto2):", resultado_diferenca)