
# 🎮 Gomoku AI Player

A Python implementation of Gomoku (Five in a Row) with an intelligent AI opponent that uses heuristic evaluation to make strategic moves.

## 🎯 What is Gomoku?

Gomoku is a classic two-player strategy board game where players take turns placing stones on a board. The first player to get **five stones in a row** (horizontally, vertically, or diagonally) wins!

## ✨ Features

- **Smart AI Opponent**: The computer evaluates board positions and chooses optimal moves
- **Pattern Detection**: Identifies open, semi-open, and closed sequences in all directions
- **Strategic Scoring**: Weighs offensive and defensive plays to maximize winning chances
- **Interactive Gameplay**: Play against the AI in your terminal
- **Board Analysis**: View detailed statistics about stone patterns after each move

## 🚀 How It Works

The AI uses a sophisticated scoring system that considers:
- **Length of sequences**: Longer chains score higher
- **Openness**: Open sequences (empty on both ends) are more valuable than blocked ones
- **Threat detection**: Prioritizes blocking opponent's winning moves
- **Offensive play**: Creates multiple threats simultaneously

### Scoring Strategy
- Five in a row = Instant win (±100,000 points)
- Four in a row = High priority (±10,000 points)
- Three in a row = Medium priority (±100 points)
- Two in a row = Low priority (±1 point)

## 🛠️ Technical Implementation

### Key Functions
- `search_max()`: Finds the best move by testing all empty positions
- `score()`: Evaluates board position strength
- `detect_rows()`: Scans all directions for stone patterns
- `is_bounded()`: Determines if a sequence is open, semi-open, or closed

### Algorithm
1. Iterates through all empty board positions
2. Simulates placing a stone at each position
3. Calculates the resulting board score
4. Selects the position with the highest score
5. Restores the board to its original state

## 🎮 How to Play

```python
# Run the game
python gomoku.py

# The AI (Black) moves first at the center
# Enter your coordinates when prompted:
# y coord: 3
# x coord: 4
```

## 📊 Board Representation

```
*0|1|2|3|4|5|6|7*
0 | | | | |w|b| *
1 | | | | | | | *
2 | | | | | | | *
3 | | | | |b| | *
4 | | | |b| | | *
5 | |w| | | | | *
6 | |w| | | | | *
7 | |w| | | | | *
*****************
```

- `b` = Black stones (AI)
- `w` = White stones (You)
- ` ` = Empty space

## 🧪 Testing

The code includes comprehensive test cases for all major functions:
```python
easy_testset_for_main_functions()  # Run all basic tests
some_tests()                        # Run scenario-based tests
```

## 🎓 Learning Highlights

This project demonstrates:
- **Game AI fundamentals**: Heuristic evaluation and move selection
- **Pattern recognition**: Multi-directional sequence detection
- **Algorithm optimization**: Efficient board scanning
- **Python programming**: List manipulation, nested loops, function design

## 🔮 Future Enhancements

- [ ] Minimax algorithm with alpha-beta pruning
- [ ] Adjustable difficulty levels
- [ ] GUI interface
- [ ] Move history and undo functionality
- [ ] Multiplayer support

## 📝 Note

This is a learning project focusing on AI game strategy. The current implementation uses a greedy approach (evaluates one move ahead). For stronger gameplay, implementing minimax with deeper search would be the next step!

---

**Built with Python** | Perfect for learning game AI concepts 🧠
