# Multi Board Tic Tac Toe With AI
This is a project that I created for the AP Computer Science Principles test. It is a python console application in which you can play tic tac toe with multiple boards. It can be played with 2 players or with an AI. It isn't so much and "AI" as an algorithm that can win whenever it is mathematically possible. This game uses the Misère rules. This means that both players play X's and the first player to make 3 in a row looses. You can play on any board you like. If 3 in a row is made on a board, it is considered dead and you can not play on it. The player that makes the final 3 in a row looses. The the first board is board '0'. The positions of the board are numbered as follows:  

    \|   \|
  0 \| 1 \| 2
 \_\_\_\|\_\_\_\|\_\_\_
    \|   \|
  3 \| 4 \| 5
 \_\_\_\|\_\_\_\|\_\_\_
    \|   \|
  6 \| 7 \| 8
    \|   \|

The algorithm that the computer uses to play against the player is based on [this paper](https://arxiv.org/pdf/1301.1672v1.pdf) by Thane E. Plambeck and Greg Whitehead
