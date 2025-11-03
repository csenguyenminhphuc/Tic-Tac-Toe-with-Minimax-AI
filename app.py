"""
Tic-Tac-Toe Web Application
Developed by: Kỹ sư Nguyễn Minh Phúc
"""

from flask import Flask, render_template, jsonify, request, session
from game_logic import GameLogic
from ai_player import AIPlayer
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)  # Secret key cho session

games = {}

# Security: Input validation
ALLOWED_DIFFICULTIES = ['easy', 'medium', 'hard']
ALLOWED_SYMBOLS = ['X', 'O']

def sanitize_input(value, allowed_values):
    """Validate and sanitize input"""
    if value not in allowed_values:
        return None
    return value

@app.route('/')
def index():
    """Render trang chủ"""
    return render_template('index.html')

@app.route('/api/new_game', methods=['POST'])
def new_game():
    """Tạo game mới - Lưu vào session"""
    try:
        data = request.json or {}
        
        # Security: Validate input
        difficulty = sanitize_input(data.get('difficulty', 'medium'), ALLOWED_DIFFICULTIES)
        player_symbol = sanitize_input(data.get('player_symbol', 'X'), ALLOWED_SYMBOLS)
        
        if not difficulty or not player_symbol:
            return jsonify({'error': 'Invalid input'}), 400
        
        ai_symbol = 'O' if player_symbol == 'X' else 'X'
        
        # Tạo game ID unique cho session
        game_id = secrets.token_urlsafe(16)
        
        # Lưu vào cả memory và session để đảm bảo persistence
        games[game_id] = {
            'logic': GameLogic(),
            'ai': AIPlayer(difficulty, ai_symbol),
            'difficulty': difficulty,
            'player_symbol': player_symbol,
            'ai_symbol': ai_symbol
        }
        
        # Lưu game state vào session
        session['game_id'] = game_id
        session['difficulty'] = difficulty
        session['player_symbol'] = player_symbol
        session['ai_symbol'] = ai_symbol
        session.modified = True
        
        return jsonify({
            'game_id': game_id,
            'board': games[game_id]['logic'].get_board(),
            'player_symbol': player_symbol,
            'ai_symbol': ai_symbol,
            'status': 'playing'
        })
    except Exception as e:
        print(f"Error in new_game: {e}")
        return jsonify({'error': 'Internal server error'}), 500

def get_game(game_id):
    """Get game từ memory hoặc recreate từ session"""
    if game_id in games:
        return games[game_id]
    
    # Nếu không có trong memory, thử recreate từ session
    if session.get('game_id') == game_id:
        try:
            # Recreate game từ session data
            difficulty = session.get('difficulty', 'medium')
            player_symbol = session.get('player_symbol', 'X')
            ai_symbol = session.get('ai_symbol', 'O')
            board_state = session.get('board', ['' for _ in range(9)])
            
            logic = GameLogic()
            logic.board = board_state.copy()
            
            games[game_id] = {
                'logic': logic,
                'ai': AIPlayer(difficulty, ai_symbol),
                'difficulty': difficulty,
                'player_symbol': player_symbol,
                'ai_symbol': ai_symbol
            }
            return games[game_id]
        except Exception as e:
            print(f"Error recreating game from session: {e}")
            return None
    
    return None

@app.route('/api/ai_first_move', methods=['POST'])
def ai_first_move():
    """AI đi nước đầu tiên (khi người chơi chọn O)"""
    try:
        data = request.json or {}
        game_id = data.get('game_id')
        
        # Security: Validate game_id
        if not game_id or not isinstance(game_id, str):
            return jsonify({'error': 'Invalid game ID'}), 400
        
        game = get_game(game_id)
        if not game:
            return jsonify({'error': 'Game not found'}), 404
        
        logic = game['logic']
        ai = game['ai']
        ai_symbol = game['ai_symbol']
        
        # AI đánh nước đầu tiên
        ai_move = ai.get_best_move(logic.get_board())
        logic.make_move(ai_move, ai_symbol)
        
        # Lưu board state vào session
        session['board'] = logic.get_board()
        session.modified = True
        
        return jsonify({
            'board': logic.get_board(),
            'ai_move': ai_move,
            'status': 'playing'
        })
    except Exception as e:
        print(f"Error in ai_first_move: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/make_move', methods=['POST'])
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
        
        game = get_game(game_id)
        if not game:
            return jsonify({'error': 'Game not found'}), 404
        
        logic = game['logic']
        ai = game['ai']
        player_symbol = game['player_symbol']
        ai_symbol = game['ai_symbol']
        
        # Kiểm tra nước đi hợp lệ
        if not logic.is_valid_move(position):
            return jsonify({'error': 'Invalid move'}), 400
        
        # Người chơi đánh
        logic.make_move(position, player_symbol)
        
        # Lưu board state vào session
        session['board'] = logic.get_board()
        session.modified = True
        
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
        
        # Lưu board state sau AI move
        session['board'] = logic.get_board()
        session.modified = True
        
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
        print(f"Error in make_move: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/reset_game/<game_id>', methods=['POST'])
def reset_game(game_id):
    """Reset game hiện tại"""
    try:
        # Security: Validate game_id
        if not game_id or not isinstance(game_id, str):
            return jsonify({'error': 'Invalid game ID'}), 400
        
        game = get_game(game_id)
        if game:
            difficulty = game['difficulty']
            player_symbol = game['player_symbol']
            ai_symbol = game['ai_symbol']
            
            # Reset game
            games[game_id] = {
                'logic': GameLogic(),
                'ai': AIPlayer(difficulty, ai_symbol),
                'difficulty': difficulty,
                'player_symbol': player_symbol,
                'ai_symbol': ai_symbol
            }
            
            # Reset board trong session
            session['board'] = games[game_id]['logic'].get_board()
            session.modified = True
            
            return jsonify({
                'board': games[game_id]['logic'].get_board(),
                'status': 'playing'
            })
        return jsonify({'error': 'Game not found'}), 404
    except Exception as e:
        print(f"Error in reset_game: {e}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
