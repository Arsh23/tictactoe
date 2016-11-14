from flask import Flask, render_template, jsonify, session
import os
import random
from copy import deepcopy
import dill
from tictactoe import TicTacToe
from alphabeta import minimax_with_alphabeta
# session['game'] = TicTacToe()
# session['ai_player'] = None
app = Flask(__name__)
app.secret_key = '*AUNSDIuasd9*ASNd*^ATSND^@R))'


@app.route('/')
def home():
    game = TicTacToe()
    session['game'] = dill.dumps(game)
    session['ai_player'] = None
    session.modified = True
    return render_template('index.html')


@app.route('/choose/<symbol>')
def choice(symbol):
    if symbol not in ['O', 'X']:
        return 'Error'
    session['ai_player'] = 'B' if symbol == 'O' else 'A'
    session.modified = True
    print 'The player for AI is -', session['ai_player']
    return session['ai_player']


@app.route('/move/<pos>')
def move(pos):
    print 'User moved -', pos
    pos = int(pos)

    game = dill.loads(session['game'])
    game.move(pos)
    game.display()
    if game.status != None:
        x = 'ai' if game.winner == session['ai_player'] else 'user'
    else:
        x = ''

    session['game'] = dill.dumps(game)
    session.modified = True
    return jsonify({
        'move': pos,
        'status': game.status,
        'winner': x,
        'winning_pos': game.winning_pos
    })


@app.route('/move_minimax')
def minimax():
    game = dill.loads(session['game'])

    pos = int(minimax_with_alphabeta(
        deepcopy(game), session['ai_player'],
        float('-inf'), float('inf'))[0])
    game.move(pos)
    game.display()
    if game.status != None:
        x = 'ai' if game.winner == session['ai_player'] else 'user'
    else:
        x = ''

    session['game'] = dill.dumps(game)
    return jsonify({
        'move': pos,
        'status': game.status,
        'winner': x,
        'winning_pos': game.winning_pos
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
