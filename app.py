from flask import Flask, render_template, jsonify
import os
import random
from copy import deepcopy

from tictactoe import TicTacToe
from alphabeta import minimax_with_alphabeta
game = TicTacToe()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/choose/<symbol>')
def choice(symbol):
    if symbol not in ['O', 'X']:
        return 'Error'
    user_player = 'A' if symbol == 'O' else 'B'
    print user_player
    return user_player

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
