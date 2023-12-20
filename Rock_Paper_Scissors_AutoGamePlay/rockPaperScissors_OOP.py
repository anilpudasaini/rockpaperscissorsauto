# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 19:13:06 2023

@author: Anil
"""

import random


class Rock:
    def __init__(self):
        self.name = "rock"

    def __str__(self):
        return self.name

    def compete(self, opponent):
        if isinstance(opponent, Scissors):
            return "Rock wins!"
        elif isinstance(opponent, Paper):
            return "Paper wins!"
        else:
            return "It's a tie!"


class Paper:
    def __init__(self):
        self.name = "paper"

    def __str__(self):
        return self.name

    def compete(self, opponent):
        if isinstance(opponent, Rock):
            return "Paper wins!"
        elif isinstance(opponent, Scissors):
            return "Scissors wins!"
        else:
            return "It's a tie!"


class Scissors:
    def __init__(self):
        self.name = "scissors"

    def __str__(self):
        return self.name

    def compete(self, opponent):
        if isinstance(opponent, Paper):
            return "Scissors wins!"
        elif isinstance(opponent, Rock):
            return "Rock wins!"
        else:
            return "It's a tie!"


choices = [Rock(), Paper(), Scissors()]


def get_user_choice():
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    while user_choice not in [choice.name for choice in choices]:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        user_choice = input("Enter rock, paper, or scissors: ").lower()
    return next((choice for choice in choices if choice.name == user_choice), None)


def get_computer_choice():
    return random.choice(choices)


def play_game():
    print("Let's play Rock-Paper-Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result = user_choice.compete(computer_choice)
        print(result)
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    play_game()
