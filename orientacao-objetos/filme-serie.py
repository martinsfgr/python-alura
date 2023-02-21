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
        return f"Série: {self._nome}, Ano: {self.ano}, Duração: {self.temporadas} minutos, Likes: {self._likes}"


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas
    
    @property
    def tamanho(self):
        return len(self._programas)


carros = Filme('carros', 2008, 120)
vingadores = Filme('vingadores - guerra infinita', 2018, 160)
demolidor = Serie('demolidor', 2016, 2)
atlanta = Serie('atlanta', 2018, 2)

carros.dar_like()
carros.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta, carros, demolidor]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

for programa in filmes_e_series:
    #detalhe = programa.duracao if hasattr(programa, "duracao") else programa.temporadas
    #print(f"{programa.nome} - {programa.ano} - {detalhe} - {programa.likes}") *sem o polimorfismo
    print(programa)

print(f"Tamanho da playlist: {playlist_fim_de_semana.tamanho}")

for programa in playlist_fim_de_semana:
    print(programa)
