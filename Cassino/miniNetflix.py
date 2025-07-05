class Series:
    def __init__(self, titulo, ano, genero):
        self.titulo = titulo
        self.ano = ano
        self.genero = genero

    def calcular_duracao(self):
        return 130  # duração padrão

    def exibir_info(self):
        print(f"\n🎬 {self.titulo} ({self.ano})")
        print(f"📚 Gênero: {self.genero}")
        print(f"⏱️ Duração estimada: {self.calcular_duracao()} min")


class Usuario:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.series_favoritas = []

    def favoritar(self, nova_serie: Series):
        if nova_serie not in self.series_favoritas:
            #Se a nova serie favoritas do Usuario nao esta contida em series favoritas
            self.series_favoritas.append(nova_serie)
            print(f"✅ '{nova_serie.titulo}' adicionada aos favoritos.")
        else:
            print("⚠️ Essa série já está na sua lista.")

    def minha_lista(self):
        print("\n📺 SÉRIES FAVORITAS:")
        if not self.series_favoritas:
            print("Nenhuma série favoritada ainda.")
        else:
            for serie in self.series_favoritas:
                print(f"- {serie.titulo} ({serie.ano})")


# Catálogo original em dict → convertido em objetos
catalogo_dict = {
    "Stranger Things": {"ano": 2016, "genero": "Ficção Científica / Suspense"},
    "Cobra Kai": {"ano": 2018, "genero": "Ação / Drama"},
    "Breaking Bad": {"ano": 2008, "genero": "Crime / Drama"},
    "The Office": {"ano": 2005, "genero": "Comédia"},
    "Sherlock": {"ano": 2010, "genero": "Mistério / Drama"}
}

# Transformar em objetos Series
catalogo = [Series(titulo, dados["ano"], dados["genero"]) for titulo, dados in catalogo_dict.items()]


def pesquisar(catalogo, termo):
    resultados = [s for s in catalogo if termo.lower() in s.titulo.lower()]
    if resultados:
        print("\n🔍 Resultados encontrados:")
        for i, serie in enumerate(resultados, 1):
            print(f"{i}. {serie.titulo} ({serie.ano})")
        return resultados
    else:
        print("Nenhuma série encontrada.")
        return []


# 🧑 Criar usuário
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
usuario = Usuario(nome, idade)

# 🎮 Loop de menu
while True:
    print("\n📺 Bem-vindo ao Mini Netflix")
    print("1. Ver catálogo")
    print("2. Pesquisar série")
    print("3. Favoritar uma série")
    print("4. Ver meus favoritos")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n🎞️ Catálogo de Séries:")
        for serie in catalogo:
            serie.exibir_info()

    elif opcao == "2":
        termo = input("Digite o nome (ou parte) da série: ")
        pesquisar(catalogo, termo)

    elif opcao == "3":
        termo = input("Digite o nome da série que deseja favoritar: ")
        encontradas = pesquisar(catalogo, termo)
        if encontradas:
            try:
                escolha = int(input("Digite o número da série para favoritar: "))
                usuario.favoritar(encontradas[escolha - 1])
            except (ValueError, IndexError):
                print("⚠️ Escolha inválida.")

    elif opcao == "4":
        usuario.minha_lista()

    elif opcao == "5":
        print("👋 Até logo!")
        break

    else:
        print("Opção inválida.")
