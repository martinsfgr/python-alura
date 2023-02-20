class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    
    def __str__(self):
        return f"Filme: {self._nome}, Ano: {self.ano}, Duração: {self.duracao} minutos, Likes: {self._likes}"


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"Filme: {self._nome}, Ano: {self.ano}, Duração: {self.temporadas} minutos, Likes: {self._likes}"

vingadores = Filme('vingadores - guerra infinita', 2018, 160)

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    #detalhe = programa.duracao if hasattr(programa, "duracao") else programa.temporadas
    #print(f"{programa.nome} - {programa.ano} - {detalhe} - {programa.likes}")

    print(programa)
