import random
import sys

users = ["meow", "moo"]
tanks = [
'frost',
'helios',
'atomic',
'toxic',
'mountain'
]

result = {}

def setup(n: int=3):
    for i in range(n):
        first_play = random.choice(users)
        first_tank = random.choice(tanks)
        second_tank = random.choice(tanks)

        result["game" + str(i + 1)] = (first_play, first_tank, second_tank)

if __name__ == "__main__":

    number_of_games = int(sys.argv[1])
    setup(number_of_games)
    first_players = [i[0] for i in list(result.values())]
    uniqueValues = set(first_players)  

    while len(uniqueValues) == 1:
        setup(number_of_games)
        first_players = [i[0] for i in list(result.values())]
        uniqueValues = set(first_players)

    for k, v in result.items():
        print(f"""\n{k}, {v[0]} plays first using {v[1]}, vs {v[2]}""")
