// Game State
let gameState = {
    gameId: null,
    difficulty: 'medium',
    playerSymbol: 'X',
    aiSymbol: 'O',
    isPlaying: false,
    stats: {
        playerWins: 0,
        aiWins: 0,
        draws: 0
    }
};

// DOM Elements
const introModal = document.getElementById('introModal');
const gameContainer = document.getElementById('gameContainer');
const resultModal = document.getElementById('resultModal');
const infoModal = document.getElementById('infoModal');
const startGameBtn = document.getElementById('startGameBtn');
const difficultyBtns = document.querySelectorAll('.difficulty-btn');
const playerBtns = document.querySelectorAll('.player-btn');
const cells = document.querySelectorAll('.cell');
const resetBtn = document.getElementById('resetBtn');
const newGameBtn = document.getElementById('newGameBtn');
const exitBtn = document.getElementById('exitBtn');
const statusMessage = document.getElementById('statusMessage');
const currentDifficulty = document.getElementById('currentDifficulty');
const playerSymbol = document.getElementById('playerSymbol');
const aiSymbol = document.getElementById('aiSymbol');
const playAgainBtn = document.getElementById('playAgainBtn');
const closeResultBtn = document.getElementById('closeResultBtn');
const infoBtn = document.getElementById('infoBtn');
const closeInfoBtn = document.getElementById('closeInfoBtn');

// Difficulty map
const difficultyMap = {
    'easy': 'Dễ',
    'medium': 'Trung bình',
    'hard': 'Khó (Bất khả thi)'
};

// Event Listeners
document.addEventListener('DOMContentLoaded', () => {
    // Difficulty selection
    difficultyBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            difficultyBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            gameState.difficulty = btn.dataset.difficulty;
        });
    });

    // Player symbol selection
    playerBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            playerBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            gameState.playerSymbol = btn.dataset.player;
            gameState.aiSymbol = btn.dataset.player === 'X' ? 'O' : 'X';
        });
    });

    // Start game
    startGameBtn.addEventListener('click', startNewGame);

    // Cell clicks
    cells.forEach(cell => {
        cell.addEventListener('click', handleCellClick);
    });

    // Control buttons
    resetBtn.addEventListener('click', resetGame);
    newGameBtn.addEventListener('click', showIntroModal);
    exitBtn.addEventListener('click', showIntroModal);
    playAgainBtn.addEventListener('click', () => {
        hideResultModal();
        resetGame();
    });
    closeResultBtn.addEventListener('click', hideResultModal);
    
    // Info button from intro modal
    infoBtn.addEventListener('click', showInfoModal);
    closeInfoBtn.addEventListener('click', hideInfoModal);
});

// Start new game
async function startNewGame() {
    try {
        const response = await fetch('/api/new_game', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                difficulty: gameState.difficulty,
                player_symbol: gameState.playerSymbol
            })
        });

        const data = await response.json();
        
        if (data.game_id) {
            gameState.gameId = data.game_id;
            gameState.isPlaying = true;
            
            // Update UI
            introModal.classList.add('hidden');
            gameContainer.classList.remove('hidden');
            currentDifficulty.textContent = difficultyMap[gameState.difficulty];
            
            // Update player symbols display
            playerSymbol.textContent = gameState.playerSymbol;
            playerSymbol.className = 'value ' + (gameState.playerSymbol === 'X' ? 'player-x' : 'player-o');
            aiSymbol.textContent = gameState.aiSymbol;
            aiSymbol.className = 'value ' + (gameState.aiSymbol === 'X' ? 'player-x' : 'player-o');
            
            // Clear board
            clearBoard();
            
            // If player chose O, AI goes first
            if (gameState.playerSymbol === 'O') {
                disableCells();
                updateStatus('AI đang đi nước đầu tiên...');
                await makeAIFirstMove();
            } else {
                enableCells();
                updateStatus('Lượt của bạn!');
            }
        }
    } catch (error) {
        console.error('Error starting game:', error);
        alert('Không thể kết nối đến server. Vui lòng kiểm tra server đã chạy chưa.');
    }
}

// AI makes first move
async function makeAIFirstMove() {
    try {
        const response = await fetch('/api/ai_first_move', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                game_id: gameState.gameId
            })
        });

        const data = await response.json();

        if (data.board) {
            updateBoard(data.board);
            if (data.ai_move !== undefined) {
                highlightCell(data.ai_move);
            }
            enableCells();
            updateStatus('Lượt của bạn!');
        }
    } catch (error) {
        console.error('Error AI first move:', error);
        enableCells();
        updateStatus('Lượt của bạn!');
    }
}

// Handle cell click
async function handleCellClick(e) {
    const cell = e.target;
    const index = parseInt(cell.dataset.index);

    if (!gameState.isPlaying || cell.textContent !== '') {
        return;
    }

    // Disable all cells while processing
    disableCells();
    updateStatus('AI đang suy nghĩ...');

    try {
        const response = await fetch('/api/make_move', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                game_id: gameState.gameId,
                position: index
            })
        });

        const data = await response.json();

        if (data.error) {
            alert(data.error);
            enableCells();
            updateStatus('Lượt của bạn!');
            return;
        }

        // Update board with player move
        updateBoard(data.board);

        // Check game status
        if (data.status === 'finished') {
            handleGameEnd(data.winner, data.winning_line);
        } else {
            // Highlight AI move
            if (data.ai_move !== undefined) {
                highlightCell(data.ai_move);
            }
            enableCells();
            updateStatus('Lượt của bạn!');
        }
    } catch (error) {
        console.error('Error making move:', error);
        alert('Lỗi khi thực hiện nước đi!');
        enableCells();
        updateStatus('Lượt của bạn!');
    }
}

// Reset current game
async function resetGame() {
    if (!gameState.gameId) return;

    try {
        const response = await fetch(`/api/reset_game/${gameState.gameId}`, {
            method: 'POST'
        });

        const data = await response.json();

        if (data.board) {
            clearBoard();
            gameState.isPlaying = true;
            
            // If player chose O, AI goes first
            if (gameState.playerSymbol === 'O') {
                disableCells();
                updateStatus('AI đang đi nước đầu tiên...');
                await makeAIFirstMove();
            } else {
                enableCells();
                updateStatus('Lượt của bạn!');
            }
        }
    } catch (error) {
        console.error('Error resetting game:', error);
        alert('Lỗi khi reset game!');
    }
}

// Update board display
function updateBoard(board) {
    cells.forEach((cell, index) => {
        const value = board[index];
        cell.textContent = value;
        
        // Remove old classes
        cell.classList.remove('x', 'o', 'winning');
        
        // Add new classes
        if (value === 'X') {
            cell.classList.add('x');
        } else if (value === 'O') {
            cell.classList.add('o');
        }
    });
}

// Clear board
function clearBoard() {
    cells.forEach(cell => {
        cell.textContent = '';
        cell.classList.remove('x', 'o', 'winning', 'disabled');
    });
}

// Enable cells
function enableCells() {
    cells.forEach(cell => {
        if (cell.textContent === '') {
            cell.classList.remove('disabled');
        }
    });
}

// Disable cells
function disableCells() {
    cells.forEach(cell => {
        cell.classList.add('disabled');
    });
}

// Highlight AI move
function highlightCell(index) {
    setTimeout(() => {
        const cell = cells[index];
        cell.style.animation = 'none';
        setTimeout(() => {
            cell.style.animation = '';
        }, 10);
    }, 100);
}

// Update status message
function updateStatus(message) {
    statusMessage.textContent = message;
}

// Handle game end
function handleGameEnd(winner, winningLine = null) {
    gameState.isPlaying = false;
    disableCells();

    let title = '';
    let message = '';

    // Draw winning line if there is one
    if (winningLine && winningLine.length === 3) {
        setTimeout(() => {
            drawWinningLine(winningLine);
        }, 100);
    }

    if (winner === gameState.playerSymbol) {
        title = '🎉 Chúc mừng!';
        message = 'Bạn đã thắng!';
        gameState.stats.playerWins++;
        updateStatus('🎉 Bạn thắng!');
    } else if (winner === gameState.aiSymbol) {
        title = '😢 Thua rồi!';
        message = 'AI đã thắng!';
        gameState.stats.aiWins++;
        updateStatus('😢 AI thắng!');
    } else {
        title = '🤝 Hòa!';
        message = 'Trận đấu hòa!';
        gameState.stats.draws++;
        updateStatus('🤝 Hòa!');
    }

    // Update stats display
    updateStatsDisplay();

    // Show result modal faster
    setTimeout(() => {
        showResultModal(title, message);
    }, 400);
}

// Draw winning line
function drawWinningLine(positions) {
    // Chỉ highlight winning cells, không vẽ đường
    positions.forEach(pos => {
        cells[pos].classList.add('winning');
    });
}

// Update stats display
function updateStatsDisplay() {
    document.getElementById('playerWins').textContent = gameState.stats.playerWins;
    document.getElementById('aiWins').textContent = gameState.stats.aiWins;
    document.getElementById('draws').textContent = gameState.stats.draws;
}

// Show result modal
function showResultModal(title, message) {
    document.getElementById('resultTitle').textContent = title;
    document.getElementById('resultMessage').textContent = message;
    resultModal.classList.remove('hidden');
}

// Hide result modal
function hideResultModal() {
    resultModal.classList.add('hidden');
}

// Show intro modal
function showIntroModal() {
    gameContainer.classList.add('hidden');
    introModal.classList.remove('hidden');
    gameState.isPlaying = false;
}

// Show info modal
function showInfoModal() {
    infoModal.classList.remove('hidden');
}

// Hide info modal
function hideInfoModal() {
    infoModal.classList.add('hidden');
}

// Keyboard shortcuts
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        if (!resultModal.classList.contains('hidden')) {
            hideResultModal();
        } else if (!infoModal.classList.contains('hidden')) {
            hideInfoModal();
        }
    }
    
    if (e.key === 'r' || e.key === 'R') {
        if (gameState.isPlaying) {
            resetGame();
        }
    }
});
