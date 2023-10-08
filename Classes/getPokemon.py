import requests

class getPokemon:
    def __init__(self):
        self.allPokemons = requests.get("https://pokeapi.co/api/v2/pokemon?limit=1292&offset=0")
        self.pokemon = "https://pokeapi.co/api/v2/pokemon/"
    def listPokemons(self):
        names = self.allPokemons.json()['results']

        print("Lista de Pokemons: ")
        for index, pokemon in enumerate(names):
            print(pokemon['name'])

    def choosedPokemon(self, choisePokemon):
        pokemonReturn = requests.get(f'{self.pokemon}{choisePokemon}')
        pokemonReturn = pokemonReturn.json()
        moves = pokemonReturn['moves']
        types = pokemonReturn['types']
        weight = pokemonReturn['weight'] / 10

        print(pokemonReturn['name'].capitalize())

        print(f"Peso: {weight} kg")

        print("Tipos: ")
        for index, type in enumerate(types):
            print(type['type']['name'])

        print("Movimentos: ")
        for index, move in enumerate(moves):
            print(move['move']['name'])