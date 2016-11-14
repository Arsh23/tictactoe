from flask import Flask, render_template, jsonify
import os
import random
from copy import deepcopy

from tictactoe import TicTacToe
from alphabeta import minimax_with_alphabeta
game = TicTacToe()
ai_player = None
app = Flask(__name__)


@app.route('/')
def home():
    global game, ai_player
    game = TicTacToe()
    ai_player = None
    return render_template('index.html')


@app.route('/choose/<symbol>')
def choice(symbol):
    global ai_player
    if symbol not in ['O', 'X']:
        return 'Error'
    ai_player = 'B' if symbol == 'O' else 'A'
    print ai_player
    return ai_player


@app.route('/move/<pos>')
def move(pos):
    if game.status == None:
        pos = int(pos)
        game.move(pos)
    game.display()
    return jsonify({
        'move': pos,
        'status': game.status,
        'winner': game.winner
    })


@app.route('/move_minimax')
def minimax():
    if game.status == None:
        print ai_player
        pos = int(minimax_with_alphabeta(
            deepcopy(game), ai_player, float('-inf'), float('inf'))[0])
        game.move(pos)
    game.display()
    return jsonify({
        'move': pos,
        'status': game.status,
        'winner': game.winner
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
