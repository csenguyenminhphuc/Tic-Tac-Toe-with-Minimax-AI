"""
Game Logic Module
Xử lý logic cơ bản của Tic-Tac-Toe
"""

class GameLogic:
    def __init__(self):
        """Khởi tạo bảng game 3x3"""
        self.board = ['' for _ in range(9)]
    
    def get_board(self):
        """Trả về trạng thái bảng hiện tại"""
        return self.board.copy()
    
    def is_valid_move(self, position):
        """Kiểm tra nước đi có hợp lệ không"""
        if position < 0 or position > 8:
            return False
        return self.board[position] == ''
    
    def make_move(self, position, player):
        """Thực hiện nước đi"""
        if self.is_valid_move(position):
            self.board[position] = player
            return True
        return False
    
    def check_winner(self):
        """
        Kiểm tra người thắng cuộc
        Returns: tuple (winner, winning_line) hoặc (None, None)
        winner: 'X', 'O', hoặc None
        winning_line: list các vị trí thắng hoặc None
        """
        # Các tổ hợp thắng
        winning_combinations = [
            [0, 1, 2],  # Hàng 1
            [3, 4, 5],  # Hàng 2
            [6, 7, 8],  # Hàng 3
            [0, 3, 6],  # Cột 1
            [1, 4, 7],  # Cột 2
            [2, 5, 8],  # Cột 3
            [0, 4, 8],  # Chéo chính
            [2, 4, 6]   # Chéo phụ
        ]
        
        for combo in winning_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] 
                and self.board[combo[0]] != ''):
                return self.board[combo[0]], combo
        
        return None, None
    
    def is_board_full(self):
        """Kiểm tra bảng đã đầy chưa"""
        return '' not in self.board
    
    def get_available_moves(self):
        """Lấy danh sách các nước đi có thể"""
        return [i for i in range(9) if self.board[i] == '']
    
    def reset(self):
        """Reset bảng game"""
        self.board = ['' for _ in range(9)]
