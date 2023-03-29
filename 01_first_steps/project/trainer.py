from typing import List

from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons: List[Pokemon] = []

    def add_pokemon(self, pokemon: Pokemon):

        if pokemon in self.pokemons:
            return f'This pokemon is already caught'
        else:
            self.pokemons.append(pokemon)
            return f'Caught {pokemon.pokemon_details()}'

    def release_pokemon(self, pokemon_name: str):
        try:
            pokemon_to_remove = list(filter(lambda x: x.name == pokemon_name, self.pokemons))[0]
            self.pokemons.remove(pokemon_to_remove)
            return f'You have released {pokemon_to_remove.name}'
        except IndexError:
            return 'Pokemon is not caught'

    def trainer_data(self):
        data_list = [f'Pokemon Trainer {self.name}', f'Pokemon caught {len(self.pokemons)}']

        data_list.extend([' - ' + x.pokemon_details() for x in self.pokemons])

        return '\n'.join(data_list)


pokemon = Pokemon("Pikachu", 90)

print(pokemon.pokemon_details())

trainer = Trainer("Ash")

print(trainer.add_pokemon(pokemon))

second_pokemon = Pokemon("Charizard", 110)

print(trainer.add_pokemon(second_pokemon))

print(trainer.add_pokemon(second_pokemon))

print(trainer.release_pokemon("Pikachu"))

print(trainer.release_pokemon("Pikachu"))

print(trainer.trainer_data())