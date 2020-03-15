import numpy as np


NUMBER_OF_DOORS = 3
NUMBER_OF_CARS = 1
NUMBER_OF_GOATS = NUMBER_OF_DOORS - NUMBER_OF_CARS


def run_simulation(
        n_plays: int,
        n_doors: int = NUMBER_OF_DOORS,
        n_cars: int = NUMBER_OF_CARS,
        make_new_choice: bool = False
):
    """run_simulation"""
    rewards = []

    for i in range(n_plays):
        reward = play_one_game(n_doors, n_cars, make_new_choice)
        rewards.append(reward)

    p_win_a_car = sum(rewards) / n_plays

    if make_new_choice is True:
        print(f"Simulate {n_plays} plays with making new decisions when showed a goat door.")
        print(f"The probability of winning a car is {p_win_a_car}.")
    else:
        print(f"Simulate {n_plays} plays without making new decisions when showed a goat door.")
        print(f"The probability of winning a car is {p_win_a_car}.")



def play_one_game(n_doors: int, n_cars: int, make_new_choice: bool):
    """
    play one monty hall game

    Args:
        n_doors(int): number of doors
        n_cars(int): number of cars
        make_new_choice(bool): if you would make a new choice upon a showed goat door

    Returns:
        reward(int): 1 if you got a car, 0 if you got a goat
    """
    doors = list(range(n_doors))
    cars = list(np.random.choice(doors, n_cars))

    choice = np.random.choice(doors, 1)[0]
    showed_goat_door = show_a_goat_door(doors, cars, choice)
    choice = make_final_decision(doors, cars, choice, showed_goat_door, make_new_choice)
    reward = get_reward(cars, choice)

    return reward


def show_a_goat_door(doors: list, cars: list, choice: int):
    """
    choose a goat door and show you the goat

    Can only choose from the goat doors that is other than your choice

    Args:
        doors(list): the list of doors
        cars(list): the list of car doors
        choice(int): the door of your choice

    Returns:
        door(int): a goat door that is other than your choice
    """
    goat_doors_to_open = [d for d in doors if d not in cars and d != choice]
    door = np.random.choice(goat_doors_to_open, 1)[0]

    return door


def make_final_decision(doors: list, cars: list, choice: int, goat_door: int, make_new_choice: bool):
    """
    showed with the goat door, make your final decision by:

    stick to your choice when make_new_choice == False
    make a new choice when make_new_choice == True

    Args:
        doors(list): the list of doors
        cars(list): the list of cars
        choice(int): the door of your choice
        goat_door(int): the showed goat door
        make_new_choice(bool): your action to make new choice or not

    Returns:
        door_of_choice(int): the door of your final decision
    """
    door_of_choice = choice

    if make_new_choice is True:
        options = [d for d in doors if d != choice and d != goat_door]
        door_of_choice = np.random.choice(options, 1)

    return door_of_choice


def get_reward(cars: list, choice: int):
    """
    get your reward according to your choice and the car doors

    Args:
        cars(list): doors of cars
        choice(int): door of your choice

    Returns:
        reward(int): 1 if you got a car, 0 if you got a goat
    """

    reward = int(choice in cars)

    return reward


if __name__ == "__main__":
    run_simulation(10000)
    run_simulation(10000, make_new_choice=True)
    run_simulation(10000, 5, 1)
    run_simulation(10000, 5, 1, True)
