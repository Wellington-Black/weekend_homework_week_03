##MVP 3: Write a game class that has a function that takes in the 2 players and compares their choices and returns the winning player. If it is a draw the player should be None type.
class Game:
   

    ##IN THIS WAY (without extra text) I CAN REUSE THE METHOD SINCE IT DOES NOT CONTAIN SPECIFIC STRINGS
     def match_2(self, player_1, player_2):
        if player_1.choice == "Rock" and player_2.choice == "Scissors":
            return player_1

        if player_1.choice == "Scissors" and player_2.choice == "Paper":
            return player_1

        if player_1.choice == "Paper" and player_2.choice == "Rock":
            return player_1
        if player_1.choice == player_2.choice:
            return "None"

        return player_2
