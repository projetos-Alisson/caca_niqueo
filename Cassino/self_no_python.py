class Series():
    def __init__(self, titulo, ano): #tirando o self, aqui ficam as variavies que receberam o valor do usuario
       #atributos que recebem o valor
        self.titulo = titulo
        self.ano = ano

    def assistir_serie(self):
        duracao = self.calcular_duracao()
        print("A série", self.titulo, "tem", duracao, "minutos de duracao.")
        print("Ano:", self.ano)

    def calcular_duracao(self):
        return 130
    
class Usuario():
    def __init__(self, nome, idade, serie_favorita: Series):
        self.nome = nome
        self.idade = idade
        self.serie_favorita = serie_favorita
        
    def favoritar(self):
     #   serie_favorita = Series.titulo
     ...

    def minha_lista(self):
        print("SÉRIES SALVAS:")
        print(self.serie_favorita.titulo)
    
#Catálogo
series = {
    "Stranger Things": {
        "ano": 2016,
        "genero": "Ficção Científica / Suspense"
    },
    "Cobra Kai": {
        "ano": 2018,
        "genero": "Ação / Drama"
    },
    "Breaking Bad": {
        "ano": 2008,
        "genero": "Crime / Drama"
    },
    "The Office": {
        "ano": 2005,
        "genero": "Comédia"
    },
    "Sherlock": {
        "ano": 2010,
        "genero": "Mistério / Drama"
    }
}


def pesquisar():
    serie_escolhida = str(input("Procurar... 🔎  "))

    for serie in series.keys():
   
        if (serie_escolhida.lower() == serie.lower()):
           print("Encontrada: ", serie_escolhida)
           return True

    print("Essa série não está no nosso catálogo")
    return False

'''PESQUISAR POR PEDAÇO DA SERIE:
def pesquisar():
    termo = input("Procurar... 🔎  ").strip().lower()
    encontrou = False

    print("\nResultados encontrados:")
    for nome in series.keys():
        if termo in nome.lower():
            print(f"- {nome} ({series[nome]['ano']}) - {series[nome]['genero']}")
            encontrou = True

    if not encontrou:
        print("Nenhuma série encontrada.")'''


pesquisar()



# Passando o objeto da classe Series para o usuário

