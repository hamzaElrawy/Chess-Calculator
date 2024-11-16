# Chess Winning Probability Calculator

## Description
The Chess Winning Probability Calculator is a Python-based project designed to calculate the winning probability for the white side in a chess game, based on the material and position of pieces on the board. The program simulates a chessboard and evaluates each piece's value and position. It uses a simple scoring system that takes into account the value of the pieces and the control over the center of the board to estimate the winning probability for white.

The program evaluates each piece on the board and calculates a material balance, which is then used to determine the winning probability for the white side. The result is displayed as a percentage, representing the likelihood of a white victory based on the current board state.

This project was primarily focused on developing the algorithm that calculates the chessboard evaluation, spending over **10 hours** working on refining and optimizing the algorithm to ensure an accurate and reliable result.

## Features
- **Piece Value Scoring**: The program assigns a numerical value to each chess piece (e.g., Queen = 9, Pawn = 1) and calculates the total material score for both white and black.
- **Position Evaluation**: The program evaluates the position of each piece on the board, considering central control as an important factor for piece effectiveness.
- **Winning Probability Calculation**: Based on the material balance and positional strength, the program calculates a probability percentage that represents the likelihood of a white victory.
- **Simple Board Representation**: The chessboard is represented as a list of 64 elements, where each element corresponds to a piece or an empty square on the board.

## How It Works
1. **Piece Values**: Each piece is assigned a specific value (e.g., King = 0, Queen = 9) to represent its strength.
2. **Position Control**: The position of each piece is evaluated based on how central or close it is to the center of the board. Pieces in central squares are generally more valuable.
3. **Calculation**: The program sums the material and position scores for both white and black, calculates the material balance, and derives a winning probability for white.

## Time Spent
The majority of the 10 hours spent on this project were dedicated to developing and refining the core **Python algorithm** that evaluates the chessboard. I focused on:
- Optimizing the piece value and position evaluation logic.
- Ensuring that the material balance and position control were accurately taken into account when calculating the probability.
- Handling edge cases and ensuring the program could work with any standard chessboard setup.

## Installation
To run the Chess Winning Probability Calculator, you'll need Python installed on your system. Follow these steps:

1. Clone the repository or download the source files.
2. Open a terminal or command prompt in the directory where the files are located.
3. Run the script by typing the following command:
   ```bash
   python chess_probability_calculator.py
 
