# Tic-Tac-Toe AI Solver

Currently, the game is **terminal-based**. The web interface is still in development. 

A robust, terminal-based implementation of Tic-Tac-Toe featuring an unbeatable AI opponent. This project demonstrates the application of adversarial search algorithms in game theory.

## 🚀 Overview
This project implements a classic 3x3 Tic-Tac-Toe game where the human player competes against a computer agent. The AI is powered by the Minimax algorithm, ensuring that if the human plays optimally, the game always ends in a draw; otherwise, the AI will win.

## 🧠 Technical Features
- **Minimax Algorithm:** Recursively evaluates every possible move to find the optimal strategy.
- **Alpha-Beta Pruning:** Optimized the search tree by eliminating branches that cannot influence the final decision, significantly improving performance.
- **Depth-Weighted Scoring:** The AI prioritizes winning in fewer moves and losing (if possible) in more moves by factoring the recursion depth into the score.
- **State Backtracking:** Efficiently explores the board state using `move()` and `undo()` methods to avoid unnecessary memory overhead.

## 📁 Project Structure
- `main.py`: Entry point containing the terminal game loop.
- `game.py`: The `Board` class handling logic, win conditions, and move validation.
- `minimax.py`: The core AI logic and recursive decision-making.

## 🕹️ How to Play
1. Ensure you have **Python 3.x** installed.
2. Clone this repository
3. ```bash
   cd ai
   python3 main.py
