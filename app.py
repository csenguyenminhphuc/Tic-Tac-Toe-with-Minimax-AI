"""
Tic-Tac-Toe Web Application
Developed by: Kỹ sư Nguyễn Minh Phúc
"""

from flask import Flask, render_template, jsonify, request, abort
from game_logic import GameLogic
from ai_player import AIPlayer
import re
from functools import wraps
from datetime import datetime, timedelta

app = Flask(__name__)

# Security: Giới hạn số game sessions
MAX_GAMES = 10000
games = {}
request_history = {}  # Track requests for rate limiting

# Security: Input validation
ALLOWED_DIFFICULTIES = ['easy', 'medium', 'hard']
ALLOWED_SYMBOLS = ['X', 'O']

def sanitize_input(value, allowed_values):
    """Validate and sanitize input"""
    if value not in allowed_values:
        return None
    return value

def rate_limit(max_requests=100, window=60):
    """Rate limiting decorator"""
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            client_ip = request.remote_addr
            current_time = datetime.now()
            
            # Clean old entries
            if client_ip in request_history:
                request_history[client_ip] = [
                    req_time for req_time in request_history[client_ip]
                    if current_time - req_time < timedelta(seconds=window)
                ]
            else:
                request_history[client_ip] = []
            
            # Check rate limit
            if len(request_history[client_ip]) >= max_requests:
                abort(429)  # Too Many Requests
            
            request_history[client_ip].append(current_time)
            return f(*args, **kwargs)
        return wrapped
    return decorator

@app.route('/')
def index():
    """Render trang chủ"""
    return render_template('index.html')

@app.route('/api/new_game', methods=['POST'])
@rate_limit(max_requests=50, window=60)
def new_game():
    """Tạo game mới"""
    try:
        data = request.json or {}
        
        # Security: Validate input
        difficulty = sanitize_input(data.get('difficulty', 'medium'), ALLOWED_DIFFICULTIES)
        player_symbol = sanitize_input(data.get('player_symbol', 'X'), ALLOWED_SYMBOLS)
        
        if not difficulty or not player_symbol:
            return jsonify({'error': 'Invalid input'}), 400
        
        # Security: Limit number of games
        if len(games) >= MAX_GAMES:
            # Clear old games
            games.clear()
        
        ai_symbol = 'O' if player_symbol == 'X' else 'X'
        
        game_id = str(len(games) + 1)
        games[game_id] = {
            'logic': GameLogic(),
            'ai': AIPlayer(difficulty, ai_symbol),
            'difficulty': difficulty,
            'player_symbol': player_symbol,
            'ai_symbol': ai_symbol
        }
        
        return jsonify({
            'game_id': game_id,
            'board': games[game_id]['logic'].get_board(),
            'player_symbol': player_symbol,
            'ai_symbol': ai_symbol,
            'status': 'playing'
        })
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/ai_first_move', methods=['POST'])
@rate_limit(max_requests=50, window=60)
def ai_first_move():
    """AI đi nước đầu tiên (khi người chơi chọn O)"""
    try:
        data = request.json or {}
        game_id = data.get('game_id')
        
        # Security: Validate game_id
        if not game_id or not isinstance(game_id, str):
            return jsonify({'error': 'Invalid game ID'}), 400
        
        if game_id not in games:
            return jsonify({'error': 'Game not found'}), 404
        
        game = games[game_id]
        logic = game['logic']
        ai = game['ai']
        ai_symbol = game['ai_symbol']
        
        # AI đánh nước đầu tiên
        ai_move = ai.get_best_move(logic.get_board())
        logic.make_move(ai_move, ai_symbol)
        
        return jsonify({
            'board': logic.get_board(),
            'ai_move': ai_move,
            'status': 'playing'
        })
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/make_move', methods=['POST'])
@rate_limit(max_requests=100, window=60)
def make_move():
    """Người chơi đánh nước"""
    try:
        data = request.json or {}
        game_id = data.get('game_id')
        position = data.get('position')
        
        # Security: Validate inputs
        if not game_id or not isinstance(game_id, str):
            return jsonify({'error': 'Invalid game ID'}), 400
        
        if not isinstance(position, int) or position < 0 or position > 8:
            return jsonify({'error': 'Invalid position'}), 400
        
        if game_id not in games:
            return jsonify({'error': 'Game not found'}), 404
        
        game = games[game_id]
        logic = game['logic']
        ai = game['ai']
        player_symbol = game['player_symbol']
        ai_symbol = game['ai_symbol']
        
        # Kiểm tra nước đi hợp lệ
        if not logic.is_valid_move(position):
            return jsonify({'error': 'Invalid move'}), 400
        
        # Người chơi đánh
        logic.make_move(position, player_symbol)
        
        # Kiểm tra thắng/thua/hòa
        winner, winning_line = logic.check_winner()
        if winner:
            return jsonify({
                'board': logic.get_board(),
                'winner': winner,
                'winning_line': winning_line,
                'status': 'finished'
            })
        
        if logic.is_board_full():
            return jsonify({
                'board': logic.get_board(),
                'winner': 'draw',
                'status': 'finished'
            })
        
        # AI đánh
        ai_move = ai.get_best_move(logic.get_board())
        logic.make_move(ai_move, ai_symbol)
        
        # Kiểm tra lại sau nước đi của AI
        winner, winning_line = logic.check_winner()
        if winner:
            return jsonify({
                'board': logic.get_board(),
                'ai_move': ai_move,
                'winner': winner,
                'winning_line': winning_line,
                'status': 'finished'
            })
        
        if logic.is_board_full():
            return jsonify({
                'board': logic.get_board(),
                'ai_move': ai_move,
                'winner': 'draw',
                'status': 'finished'
            })
        
        return jsonify({
            'board': logic.get_board(),
            'ai_move': ai_move,
            'status': 'playing'
        })
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/reset_game/<game_id>', methods=['POST'])
@rate_limit(max_requests=50, window=60)
def reset_game(game_id):
    """Reset game hiện tại"""
    try:
        # Security: Validate game_id
        if not game_id or not isinstance(game_id, str):
            return jsonify({'error': 'Invalid game ID'}), 400
        
        if game_id in games:
            difficulty = games[game_id]['difficulty']
            player_symbol = games[game_id]['player_symbol']
            ai_symbol = games[game_id]['ai_symbol']
            games[game_id] = {
                'logic': GameLogic(),
                'ai': AIPlayer(difficulty, ai_symbol),
                'difficulty': difficulty,
                'player_symbol': player_symbol,
                'ai_symbol': ai_symbol
            }
            return jsonify({
                'board': games[game_id]['logic'].get_board(),
                'status': 'playing'
            })
        return jsonify({'error': 'Game not found'}), 404
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
