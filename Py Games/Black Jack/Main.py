import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def start_deck():
    players = []
    for i in range(2):
        rand_card = random.choice(cards)
        players.append(rand_card)
    return players


def add_card(add):
    rand_card = random.choice(cards)
    add.append(rand_card)
    return add


if __name__ == "__main__":
    computer = start_deck()
    player = start_deck()
    print(f"Your Cards: {player}, current score: {sum(player)}")
    print(f"computer's First card: {computer[0]}")
    while True:
        random_integer = random.randrange(2)
        p_input = input("Type 'y' to get another card, type 'n' to pass: ")
        if random_integer == 0:
            add_card(computer)
        sum_player = sum(player)
        sum_computer = sum(computer)
        if p_input == 'y':
            add_card(player)
            print(f"Your Cards: {player}, current score: {sum(player)}")
            print(f"computer's summ card: {sum_computer}")

            if sum_player > 21 > sum_computer:
                print(f"you went over your score is {sum_player}")
                break
            elif sum_player < 21 < sum_computer:
                print(f"Computer went over your score is {sum_player}")
                print(f"computer score is {sum(player)}")

        if p_input == 'n':
            if sum_player > 21 > sum_computer:
                print(f"you went over your score is {sum_player}")
                break
            elif sum_player < 21 < sum_computer:
                print(f"Computer went over your score is {sum_player}")
                print(f"computer score is {sum(player)}")



