piece_values = {
    "♕": 9, "♛": 9,
    "♖": 5, "♜": 5,
    "♗": 3, "♝": 3,
    "♘": 3, "♞": 3,
    "♙": 1, "♟": 1,
    "♔": 0, "♚": 0  
}

def evaluate_position(piece, position, color):
    row = position // 8
    col = position % 8

    center_control_bonus = (3 - abs(3 - row)) + (3 - abs(3 - col))

    if piece == "♞" or piece == "♘":
        return center_control_bonus * 2  
    return center_control_bonus

def calculate_winning_probability(board):
    white_score = 0
    black_score = 0
    white_position_score = 0
    black_position_score = 0


    for i in range(64):
        piece = board[i]
        if piece in piece_values:
            if piece == piece.upper():  
                white_score += piece_values[piece]
                white_position_score += evaluate_position(piece, i, 'white')
            else:  
                black_score += piece_values[piece]
                black_position_score += evaluate_position(piece, i, 'black')

    total_score = white_score + black_score
    if total_score == 0:
        return 50  


    material_balance = (white_score / total_score) * 100
    material_balance += (white_position_score - black_position_score) / total_score * 10

    return round(material_balance, 2)


sample_board = [
    "♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖",
    "♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙",
    "", "", "", "", "", "", "", "",
    "", "", "", "", "", "", "", "",
    "", "", "", "", "", "", "", "",
    "", "", "", "", "", "", "", "",
    "♟", "♟", "♟", "♟", "♟", "♟", "♟", "♟",
    "♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"
]


winning_probability = calculate_winning_probability(sample_board)
print(f"Winning Probability (White): {winning_probability}%")
