"""
AI Player Module
Triển khai thuật toán Minimax với alpha-beta pruning
3 mức độ: Dễ (random), Trung bình (minimax giới hạn), Khó (minimax đầy đủ)
"""

import random
from game_logic import GameLogic

class AIPlayer:
    def __init__(self, difficulty='medium', ai_symbol='O'):
        """
        difficulty: 'easy', 'medium', 'hard'
        ai_symbol: 'X' hoặc 'O' - ký hiệu AI sử dụng
        """
        self.difficulty = difficulty
        self.ai_symbol = ai_symbol
        self.player_symbol = 'X' if ai_symbol == 'O' else 'O'
    
    def get_best_move(self, board):
        """Lấy nước đi tốt nhất dựa trên độ khó"""
        available_moves = [i for i in range(9) if board[i] == '']
        
        if not available_moves:
            return None
        
        # Nếu là nước đầu tiên (bảng trống), chọn ngẫu nhiên cho tất cả độ khó
        if len(available_moves) == 9:
            return random.choice(available_moves)
        
        if self.difficulty == 'easy':
            return self._get_easy_move(board, available_moves)
        elif self.difficulty == 'medium':
            return self._get_medium_move(board, available_moves)
        else:  # hard
            return self._get_hard_move(board, available_moves)
    
    def _get_easy_move(self, board, available_moves):
        """Mức dễ: Chọn ngẫu nhiên"""
        return random.choice(available_moves)
    
    def _get_medium_move(self, board, available_moves):
        """Mức trung bình: 70% minimax, 30% random"""
        if random.random() < 0.7:
            return self._get_hard_move(board, available_moves)
        else:
            return random.choice(available_moves)
    
    def _get_hard_move(self, board, available_moves):
        """Mức khó: Minimax với alpha-beta pruning (bất khả thi)"""
        best_score = float('-inf')
        best_move = available_moves[0]
        
        for move in available_moves:
            # Thử nước đi
            board[move] = self.ai_symbol
            score = self._minimax(board, 0, False, float('-inf'), float('inf'))
            board[move] = ''
            
            if score > best_score:
                best_score = score
                best_move = move
        
        return best_move
    
    def _minimax(self, board, depth, is_maximizing, alpha, beta):
        """
        Thuật toán Minimax với alpha-beta pruning
        is_maximizing: True nếu là lượt AI, False nếu là lượt người chơi
        """
        # Kiểm tra trạng thái kết thúc
        winner = self._check_winner(board)
        
        if winner == self.ai_symbol:
            return 10 - depth  # AI thắng, ưu tiên thắng nhanh
        elif winner == self.player_symbol:
            return depth - 10  # Người chơi thắng
        elif self._is_board_full(board):
            return 0  # Hòa
        
        available_moves = [i for i in range(9) if board[i] == '']
        
        if is_maximizing:
            # Lượt AI - tối đa hóa điểm
            max_eval = float('-inf')
            for move in available_moves:
                board[move] = self.ai_symbol
                eval_score = self._minimax(board, depth + 1, False, alpha, beta)
                board[move] = ''
                max_eval = max(max_eval, eval_score)
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break  # Alpha-beta pruning
            return max_eval
        else:
            # Lượt người chơi - tối thiểu hóa điểm
            min_eval = float('inf')
            for move in available_moves:
                board[move] = self.player_symbol
                eval_score = self._minimax(board, depth + 1, True, alpha, beta)
                board[move] = ''
                min_eval = min(min_eval, eval_score)
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break  # Alpha-beta pruning
            return min_eval
    
    def _check_winner(self, board):
        """Kiểm tra người thắng"""
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Hàng
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Cột
            [0, 4, 8], [2, 4, 6]               # Chéo
        ]
        
        for combo in winning_combinations:
            if (board[combo[0]] == board[combo[1]] == board[combo[2]] 
                and board[combo[0]] != ''):
                return board[combo[0]]
        
        return None
    
    def _is_board_full(self, board):
        """Kiểm tra bảng đầy"""
        return '' not in board
