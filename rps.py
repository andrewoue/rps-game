#!/usr/bin/env python3

#RPS Udacity Project 1.0, Andrew Ouellette

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""

import random

class Player:
    def move(self):
        pass

    def learn(self, my_move, their_move):
        pass
#Parent Player Class

class HumanPlayer(Player):
    def move(self):
        decision = input("Choose wisely... rock, paper, or scissors. ").lower()
        while decision != "rock" and decision != "paper" and decision != "scissors":
            print("I don't understand, please try again.")
            decision = input('rock, paper, or scissors... ')
        return decision
#Human Player class

class RockPlayer(Player):
    def move(self):
        return moves[0]
#This Player class always selects rock

class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)
#This Player class selects a random move

class CyclePlayer(Player):
    def move(self):
        return moves[Game.round_count]
#This Player class follows the order - rock, paper, scissors

class CopyPlayer(Player):
    def move(self):
        if Game.round_count == 0:
            return random.choice(moves)
        elif Game.round_count == 1:
            return Game.p1_move_list[0]
        else:
            return Game.p1_move_list[1]

    def learn(self, my_move, their_move):
        my_move = Game.p2_move_list
        thier_move = Game.p1_move_list
#This Player class copies the Human Player class selections

def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

def select_opponent():
    cpu_player_list = (RockPlayer, RandomPlayer, CyclePlayer, CopyPlayer)
    cpu_player = random.choice(cpu_player_list)
    return cpu_player()
#Random selection of CPU Player sub class

class Game:
    game_count = 0
    round_count = 0
    p1_move_list = []
    p2_move_list = []

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1.score = 0
        self.p2.score = 0

    def game_select(self):
        games = input("Let's play Rock, Paper, Scissors! 1 or 3 rounds? ")
        while games != "1" and games != "3":
            print("I don't understand, please try again.")
            games = input("1 or 3? ")
        Game.game_count = int(games)
    #Allows player to select between a single round or three rounds

    def play_round(self):
        move1 = self.p1.move()
        Game.p1_move_list.append(move1)
        move2 = self.p2.move()
        Game.p2_move_list.append(move2)
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            print("*** PLAYER ONE WINS ***")
            self.p1.score += 1
        elif beats(move2, move1):
            print("*** PLAYER TWO WINS ***")
            self.p2.score += 1
        else:
            print("*** IT'S A TIE ***")
        print(f"The score is {self.p1.score} to {self.p2.score}")
        Game.round_count += 1

    def play_game(self):
        print("*** GAME START ***")
        for round in range(self.game_count):
            print(f"Round {round + 1}:")
            self.play_round()
        print("*** GAME OVER ***")
        if self.p1.score > self.p2.score:
            print("*** PLAYER ONE WINS THE GAME ***")
        elif self.p2.score > self.p1.score:
            print("*** PLAYER TWO WINS THE GAME ***")
        else:
            print("*** THIS GAME IS A TIE ***")
        print(f"*** FINAL SCORE: {self.p1.score} TO {self.p2.score} ***")

if __name__ == '__main__':
    game = Game(HumanPlayer(), select_opponent())
    game.game_select()
    game.play_game()
