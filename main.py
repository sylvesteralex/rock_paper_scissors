from random import choice
from rock_paper_scissors_helpers import rock_paper_scissors_pics
from rock_paper_scissors_helpers import hand
from rock_paper_scissors_helpers import menu_action_prompt


def main():
    print("== Rock, paper, scissors game ==")
    action = None

    while action != "exit":
        action = menu_action_prompt()

        if action == "E":
            break
        elif action == "S":
            points = 0
            opponent_points = 0
            rock_paper_scissors(points, opponent_points)
            menu_action_prompt()
        else:
            menu_action_prompt()

        break


def drawing_hand(hand):
    given_hand = hand
    hand_drawing = None

    if given_hand == "rock":
        hand_drawing = rock_paper_scissors_pics[0]
    elif given_hand == "paper":
        hand_drawing = rock_paper_scissors_pics[1]
    elif given_hand == "scissors":
        hand_drawing = rock_paper_scissors_pics[2]

    return hand_drawing


def rock_paper_scissors(points, opponent_points):

    player_hand = input("What's you choice?: ")

    if player_hand not in hand:
        print(f"You can only choose {hand}")
        player_hand = input("What's you choice?: ")

    print(drawing_hand(player_hand))
    ai_hand = choice(hand)
    print(f"Your opponent hand is: {ai_hand}")
    print(drawing_hand(ai_hand))

    def results():
        if player_hand == "rock" and ai_hand == "scissors":
            return "You won!"
        elif player_hand == "rock" and ai_hand == "paper":
            return "You lost!"
        elif player_hand == "rock" and ai_hand == "rock":
            return "It's a tie!"
        elif player_hand == "paper" and ai_hand == "paper":
            return "It's a tie!"
        elif player_hand == "paper" and ai_hand == "rock":
            return "You won!"
        elif player_hand == "paper" and ai_hand == "scissors":
            return "You lost!"
        elif player_hand == "scissors" and ai_hand == "paper":
            return "You won!"
        elif player_hand == "scissors" and ai_hand == "rock":
            return "You lost!"
        elif player_hand == "scissors" and ai_hand == "scissors":
            return "It's a tie!"

    print("=" * 8)
    print(results())
    print("=" * 8)

    if results() == "You won!":
        points += 1
    elif results() == "You lost!":
        opponent_points += 1

    print(f"Your points: {points}")
    print(f"Your opponent's points: {opponent_points}")
    print("=" * 8)

    cont = str(input("Do you want to play another round? (Y/N): ")).strip().upper()[0]

    while cont != "N":
        if cont == "Y":
            rock_paper_scissors(points, opponent_points)
        elif cont == "N":
            break
        else:
            print("Command not recognized! You will return to the menu shortly.")

        break


if __name__ == '__main__':
    main()
