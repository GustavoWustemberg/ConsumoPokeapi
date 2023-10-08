from Classes.getPokemon import getPokemon

getPokemon = getPokemon()

while True:
    x = int(input("1 - Ver a lista dos pokemons disponíveis\n2 - Pesquisar Pokemon\n"))
    if x == 1:
        getPokemon.listPokemons()
    elif x == 2:
        chosePokemon = input("Qual pokemon deseja ver? ")
        getPokemon.choosedPokemon(chosePokemon)
    else:
        break