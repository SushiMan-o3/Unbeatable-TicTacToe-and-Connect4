# Overview
Connect 4 and Tictactoe with a minimax implementation and a random move implmentation such that the client can choose to either play a bot that chooses random moves or a bot that plays every move perfectly and wins or draws every game that is played. The connect four game contains alpha beta pruning to make it faster by remove unnesscary trees.\

# Set Up
Honestly, I have no idea how you should set it up, but you can just import the python file and create an instance `PlayProBot()` and simple call `start()` on that instance. Given this, it should start a game for you. This works for both bots. 

# Connect 4 Bot
The Pro Connect 4 bot evaluates a given position based on where a coin has been dropped. Given this, it gives points based on its proximity to the middle column (col 3) and how close the bot is to obtaining a win. As a result, it is able to generate a decent understanding of what needs to be placed. When minimaxing, it is noted that the depth of the move is also considered for obtaining the best move as a win that can be reached is 2 moves is always better than a win that can be obtained in 3 moves. As a result, the bot is optimized to play the best move each and every play, ensuring that it tries its best to win and not lose or draw the game.

Alpha-beta pruning is used in the minimaxing step to ensure that moves that are worse than the current best move is not evaluated thus making the bot signficantly faster. 

# TicTacToe Bot
The Tictactoe bot is made using a simply just handles wins and loses using minimax. It is noted that the depth of the minimax is set to 9 when playing against as there are less possibities in a tictactoe game thus meaning it will always be fast. As a result, a simple system without an evaluation tool was used to create the tictactoe pro bot. 
