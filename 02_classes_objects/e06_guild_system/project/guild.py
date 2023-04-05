from typing import List
from project.player import Player

class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players: List[Player] = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f'Player {player.name} is already in the guild.'

        if player.guild != Player.DEFAULT_GUILD:
            return f'Player {player.name} is in another guild.'

        self.players.append(player)
        player.guild = self.name
        return f'Welcome player {player.name} to the guild {self.name}'

    def kick_player(self, player_name: str):
        try:
            index_to_remove = self.players.index(list(filter(lambda x: x.name == player_name, self.players))[0])
            self.players[index_to_remove].guild = Player.DEFAULT_GUILD
            del self.players[index_to_remove]

            return f'Player {player_name} has been removed from the guild.'
        except IndexError:
            return f'Player {player_name} is not in the guild.'

    def guild_info(self):
        players_info = '\n'.join([x.player_info() for x in self.players])

        return f'Guild: {self.name}\n' \
            f'{players_info}'


# player = Player("Pesho", 90, 90)
# player.add_skill("A", 3)
# player.add_skill("B", 6)
# print(player.player_info())
# # print(player.skills)
