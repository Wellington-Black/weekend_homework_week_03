## MVP2: Write a class to represent the player. The player will have a name and their choice (rock/paper/scissors).
import random
class Player:
    
    def __init__(self, name=None, choice=None, number=None):
        
        self.name = name
        self.choice = choice
        self.number = number

    @classmethod
    def computer_player(cls):
        return cls(
            "Computer",
            random.choice(["Rock", "Paper", "Scissors"])
        )
