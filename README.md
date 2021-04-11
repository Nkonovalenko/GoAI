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

# Current Goals for Implementation:
- Minimax Agent that implements Alpha-Beta pruning to reduce search width
- Non-Naive Agent which will use a Convolutional Neural Network
- Developing a front-end for the GoAI
- Deploying the GoAI to AWS so that it can compete online

# Lessons Learned Thus Far
- Naive algorithms are very fast, but do not produce results
- Minimax produces results, but is far too slow to be able to train and use easily
- Thus, optimization is a very important aspect of Artificial Intelligence
