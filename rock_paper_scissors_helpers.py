# menu prompt
def menu_action_prompt():
    print("=" * 8)
    menu_action = str(input("(S)tart a new game or (E)xit. (Type S or E): ")).strip().upper()[0]
    return menu_action

# players choice
hand = ("rock", "paper", "scissors")

# choice pics
rock_paper_scissors_pics = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

    ''', '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

    ''', '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

    ''']
