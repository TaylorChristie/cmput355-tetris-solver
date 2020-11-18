## Notes
implement a simple python solver that will solve based on a certain heuristic and bruteforce placement of pieces
heuristics
 - distance from top
 - minimize open spaces (empty blocks with blocks above)
 - combination of the two?

will need to actually play via pygame and not block the ticker or slow the game down, but this shouldnt be an issue since there are only a couple of possible placement locations that are actually valid

left to right with all rotation combinations, choose the best option


If time allows, 
implement an AI algorithm (genetic based) building off of the previous solver



--- 

 Because I didn't want to implement the game, I used this tutorial: https://levelup.gitconnected.com/writing-tetris-in-python-2a16bddb5318


for actual AI need weighing on a variety of heuristics