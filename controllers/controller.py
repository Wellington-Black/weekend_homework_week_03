from flask import render_template, request
from app import app
from models import game
from models import player
from models.players import *
from models.games import *




@app.route('/')
def home():
    return render_template('layout.html')


## MVP 1: You should be able to go to /rock/scissors and return the string "Player 1 wins by playing rock" to the page, for example.

@app.route('/<choice_1>/<choice_2>')
def play(choice_1, choice_2):
    #Set variables and order based on choice
    player_1.choice = choice_1  
    player_2.choice = choice_2
    player_1.number = 1
    player_2.number = 2
    return render_template('game1.html', title='Game', player_1=player_1, player_2=player_2, game_1=game_1)

## MVP4: Change your route to use a template to display the users choices and the result.
@app.route('/play2/<choice_1>/<choice_2>')
def play_2(choice_1, choice_2):
    #Set variables and order based on choice
    player_1.choice = choice_1  
    player_2.choice = choice_2
    player_1.number = 1
    player_2.number = 2
    return render_template('users_choices.html', title='Game', player_1=player_1, player_2=player_2, game_1=game_1)

## EXTENSIONS 1: Add a welcome page (and a route to get it) to explain the rules before the user picks their move. Add a link to this in the base template.
@app.route('/home')
def h():
    return render_template('home.html')

@app.route('/rules1')
def rules1():
    return render_template('rules1.html')
@app.route('/rules')
def rules():
   
    return render_template('rules1.html', title="Rules", player_1=player_1, player_2=player_2, game_1=game_1)

##FURTHER EXTENSION:
# If they go to /play it will take the user to a form to allow them to enter their name and choose a move from a dropdown.
# Add a link to this page to the base template.
# Write a new method in the game class to generate a computer player with the name "Computer" and a random choice from rock, paper and scissors. (Look into the random.choice) library.

@app.route('/play')
def computer_play():
         
    return render_template('play.html', title="Game")


@app.route('/winner', methods=['GET', 'POST'])
def winner():
    player_1.name = request.form['name']
    player_1.choice = request.form['choice']
    player_2 = Player()
    player_2 = Player.computer_player()

    return render_template('winner.html',title="Winner", player_1=player_1, player_2=player_2, game_1=game_1)