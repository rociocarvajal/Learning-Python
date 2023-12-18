# Game 
import random

def play():
    user = input("Choose one: 'scissor', 'stone' or 'paper'.\n").lower() 
    # metodo lower convierte string en miniscula, estilo strtolower() en php
    pc = random.choice(['scissor', 'stone', 'paper'])

    if user == pc:
        return 'Tie'
    
    if winner(user, pc):
        return 'Won'
    
    return 'You lost'


def winner(player, opponent):
    # Retorna true si gano el jugador
    if ((player == 'stone' and opponent == 'scissor')
        or (player == 'scissor' and opponent == 'paper')
        or (player == 'paper' and opponent == 'stone')):
        return True
    else:
        return False
    

print(play())