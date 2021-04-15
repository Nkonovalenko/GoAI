# GoAI

This past academic year I completed Machine Learning and Computer Vision courses at the University of Michigan. These led me to become interested in Artificial Intelligence, which will be another class I take in the upcoming fall. However until then I've decided to work on a project for my own curiosity, a bot that can play Go. 

This AI will be written in Python, and in later stages of the project will be deployed to AWS so that I can test it against other players and AI's.

# Currently Implemented:
- Classes to handle the GameState, Game, Board, Player, Move, Point
- Checking superko is done through storing every GameState and iterating through them for each move (very inefficient, goboard_slow.py)
- Naive Agent which creates a list of every move it can make that preserves its "eyes", and chooses one at random
- Zobrist Hashing which stores the GameStates as hashes, making goboard.py more efficient than goboard_slow.py.
- Minimax Agent which creates a list of every legal move, and then uses finds the best possible scenario
- Depth Pruned Minimax Agent which is more efficient than Minimax agent. It uses an evaluation function to prune the total number of branches.
- Minimax Agent that implements Alpha-Beta pruning to reduce search width
- MCTS Agent that will simulate games randomly

# Current Goals for Implementation:
- Optimize my RandomBot so that it can be used for easily for the MCTS simulations
- Optimize my goboard
- Agent which will use multilayer perceptron
- Agent which will use a Convolutional Neural Network
- Developing a front-end for the GoAI
- Deploying the GoAI to AWS so that it can compete online


# Lessons Learned Thus Far
- Naive algorithms are very fast, but do not produce results
- Minimax produces results, but is far too slow to be able to train and use easily
- Thus, optimization is a very important aspect of Artificial Intelligence

# Currently Implemented Algorithms Explained
## Convolutional Neural Network (coming soon)
- This model type will likely be better than Perceptron, as it is built to analyze spatial relationships

## Multilayer Perceptron
- This is the first machien learning algorithm I'll be implementing
- It takes in a set of data, splits it into train/test, and converts the 9x9 input into size 81 vectors
- This model will have 3 dense layers, with 81 output classes
- Out Perceptron algorithm doesn't understand the rules, and ocassionally recommends unavailable moves
- It prefers moves played at the center of the board as opposed to the edges
- Flattening the input results in information being lost, thus Perceptron is not the best model architecture for Go. 

## Monte Carlo Tree Search
- Monte Carlo algorithms use randomness to analyze complex positions
- Our Minimax Algorithms evaluate positions with a simplistic heuristic that won't do well against experienced players
- MCTS allows for an evaluation of positions without strategic knowledge through using random simulations
- From any given position, it will build a tree and evaluate how many times each color wins, choosing the move that results in the most wins
- Each iteration of the MCTS has three steps:
   1) Add new position to tree
   2) Simulate random game from that position
   3) Update tree statistics with results of that game
- MCTSAgent is faster than the previous algorithm, taking just under 3 minutes for the first move
 
## Minimax with Alpha Beta Pruning
- This algorithm attempts to minimize the pain in a max loss scenario
- As seen below, Minimax with Depth Pruning is incredibly slow still
- Alpha Beta Pruning keeps track of the best outcome for white (Alpha), and black (Beta)
- If a branch better than Alpha for white, or Beta for black appears, we will continue analysing it
- If a branch worse than Alpha for white, or Beta for black appears, we don't need to look further
- This means we only consider branches AT LEAST as good as the best so far, allowing us to prune worse branches
- For the first move, this agent took just under 4 minutes, which is still not really as efficient as what we want.

## Minimax with Depth Pruning
- This algorithm attempts to minimize the pain in a max loss scenario
- It contains the strengths of Minimax, while improving on the weakness of speed
- It drastically improves the runtime by pruning branches beyond a pre-specified depth
- While testing this on a 5x5 board, after my first move, the algorithm had 26 possible moves
- To compute the best move to a depth of 3 moves, it took 4 minutes
- While it is much faster than Minimax, 4 minutes for a depth of 3 is not nearly as efficient as what we want

## Minimax
- This algorithm attempts to minimize the pain in a max loss scenario
- It attempts to find the best move for itself, then the best move for the bot, and keeps alternating
- A big strength is that theoretically it is impossible for this algorithm to lose
- A big weakness is that this algorithm is extremely slow as it constructs an extremely large tree

## Naive Algorithm
- This algorithm is based on preserving the bot's own "eyes"
- It loops through every single possible move, and checks whether it is legal and preserves the "eyes"
- If so, it is then appended to a list of legal moves, which the AI then chooses one at random
