# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 19:04:52 2023

@author: Anil
"""

import random

choices = ["rock", "paper", "scissors"]


def get_user_choice():
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    while user_choice not in choices:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        user_choice = input("Enter rock, paper, or scissors: ").lower()
    return user_choice


def get_computer_choice():
    return random.choice(choices)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"


def play_game():
    print("Let's play Rock-Paper-Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    play_game()
