# GoAI

This past academic year I completed Machine Learning and Computer Vision courses at the University of Michigan. These led me to become interested in Artificial Intelligence, which will be another class I take in the upcoming fall. However until then I've decided to work on a project for my own curiosity, a bot that can play Go. I found a great book that will teach me about Go, the algorithms, and the development of an end to end system that will allow my GoAI to have a frontend and backend hosted on AWS. Completion of this project will give me the skills necessary to implement these algorithms for other games such as Chess.

This AI will be written in Python, and in later stages of the project will be deployed to AWS so that I can test it against other players and AI's.

I'm very excited with how the AI has been improving thus far in my journey. At first the AI played only random moves, but I believe that I am close to completing a neural network that trains on high level player games. I have realized that currently my laptop is bottlenecking the training of my CNN, so I am currently requesting approval for an AWS EC2 instance where I would be able to take advantage of TensorFlow's GPU acceleration.

The request for an AWS EC2 instance has been approved. I will be using a Deep Learning Ubuntu AMI, specifically a p2.xlarge instance. P2's have 4 vCPU's, 31 GiB memory, and support TensorFlow GPU acceleration.

# Currently Implemented:
- Classes to handle the GameState, Game, Board, Player, Move, Point
- Checking superko is done through storing every GameState and iterating through them for each move (very inefficient, goboard_slow.py)
- Naive Agent which creates a list of every move it can make that preserves its "eyes", and chooses one at random
- Zobrist Hashing which stores the GameStates as hashes, making goboard.py more efficient than goboard_slow.py.
- Minimax Agent which creates a list of every legal move, and then uses finds the best possible scenario
- Depth Pruned Minimax Agent which is more efficient than Minimax agent. It uses an evaluation function to prune the total number of branches.
- Minimax Agent that implements Alpha-Beta pruning to reduce search width
- MCTS Agent that will simulate games randomly
- Agent which uses multilayer perceptron
- Agent which uses a convolutional neural network
- Downloading Go data from the KGSIndex which has high level games that will be better training data than random MCTS training data
- A DataProcessor class that is able to unzip contents of the downloaded data, and encode it

# Current Goals for Implementation:
- Developing a front-end for the GoAI
- Deploying the GoAI to AWS so that it can compete online
- Training GoAI on AWS using TensorFlow GPU acceleration
- I now have an EC2 instance set up, I need to train the model on it.
- Figure out how to make the bot communicate with other bots


# Lessons Learned Thus Far
- Naive algorithms are very fast, but do not produce results
- Minimax produces results, but is far too slow to be able to train and use easily
- Thus, optimization is a very important aspect of Artificial Intelligence\
- My neural networks thus far have been trained on games I generated using MCTS agents
- This essentially means the moves it trains on are nearly random, and a 20% validation accuracy will not perform well against strong players
- For this reason I have to find a data source of Go games from strong players to train on, in order to "learn" the strategies of the game
- A neural network's accuracy is limited by the quality of the data that it trains on.
- TensorFlow with GPU acceleration would greatly speed up training speed, I'll be looking into AWS or Google Colab.

# Currently Implemented Algorithms Explained
## Convolutional Neural Network (Trained on high level games)
- I have create several classes for Data importing, processing, and encoding that allow me to download high level games.
- I then am able to choose the number of games I want to train on, out of over 17,000 available games.
- The network layers are in networks/small.py, I use Conv2D with MaxPooling and ReLU activation.
- It uses cross entropy loss with the stochastic gradient descent optimizer. It might be possible to speed up results with AdaGrad.
- With 100 games and a batch size of 128, our model has 88 steps per epoch.
   1) After 100 epochs: 0.42% accuracy
   2) After 250 epochs: 2.81% accuracy
   3) After 500 epochs: 33.34% accuracy
   4) After 750 epochs: 90.64% accuracy
   5) Highest accuracy reached epoch 965: 98.7%
- One thing to keep in mind for the above results, the network trained on an incredibly small number of games
- In order for this AI to reach a level where it plays better, it much be trained on preferably 10,000 games.
- My laptop does not support TensorFlow GPU acceleration, thus I must find a way to train either on Google Colab or AWS.

## Convolutional Neural Network (Trained on randomly generated moves)
- This model type will likely be better than Perceptron, as it is built to analyze spatial relationships
- Using Cross Entropy Loss which is much better for classification problems
- After training for 100 epochs, we have an accuracy of 7.57% which is 3.35x better than the Multilayer Perceptron
- After training for 500 epochs, we have an accuracy of 19.69%, which is 8.73x better than the Multilayer Perceptron


## Multilayer Perceptron
- This is the first machine learning algorithm I'll be implementing
- It takes in a set of data, splits it into train/test, and converts the 9x9 input into size 81 vectors
- This model will have 3 dense layers, with 81 output classes
- Out Perceptron algorithm doesn't understand the rules, and ocassionally recommends unavailable moves
- It prefers moves played at the center of the board as opposed to the edges
- Used Mean Square Error for loss, which is better for regression problems (not the best choice for this task)
- After training 363,000 boards we get a test accuracy of 2.256%, for perspective randomly guessing results in 1.23%.
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
