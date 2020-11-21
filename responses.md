# Question Responses
## 1. 
tsc2
## 2. 
Taylor Christie, 1528468, tsc2
## 3. 
Well, I did the entire project myself with no external help (other than some research and a previously programmed version of the game so I didn't have to write it myself). I feel like I performed to my expectations in this project.
## 4. 
I used code that was created by someone else for the actual python game of tetris that can be found here: https://levelup.gitconnected.com/writing-tetris-in-python-2a16bddb5318. Full disclosure, there is also a tutorial about writing a python "ai" as a secondary article, but I did not use any of his code in the writing of my solver and only did research from other sources such as https://github.com/mzmousa/tetris-ai to see what sort of criteria people were using to determine best placement of pieces. All the solver code was written solely by me. My code repository can be found at: https://github.com/TaylorChristie/cmput355-tetris-solver. The repository has a video file 
## 5. 
The game I decided to write a solver for is tetris. Basically, the object of the game is to stack 7 different types of randomly generated blocks together to obtain points and stay alive as long as possible. while they drop at increasingly faster speeds. See https://en.wikipedia.org/wiki/Tetris for more contextual information, but I think most people have played tetris at least once.
## 6. 
In this project I spent a lot of time thinking about the best ways to compute the best possible move for a given board and piece. Because tetris is a game that is computationally plausible to solve in real time, I don't need to worry too much about determining a fast algorithm to find best moves like other games such as Go or Chess, so I could take the "brute force" approach on all valid game moves and determine based off a set of properties what is the best move. 

My original goals for this project was to get the solver to play tetris indefinitely, because I thought that would be relatively easy to accomplish - however that turned out to not be the case after starting to write the solver and understanding the statistics behind "computing the best move". After I determined indefinite play might be a lofty goal, I switched to having the solver play like an intermediate tetris player - which I think I have achieved.

The most satisfying part of the project is to see the blocks place in positions you expect them to place to make the best move. I can't quite explain it, but to give the computer enough information to make an informed move based solely on board position statistics is actually pretty cool. I knew I picked the right game, because as soon as I saw the blocks placing with intent to clear or not to block holes, I was ecstatic. 

The most disappointing or frustrating part of the project would probably be dealing with the data structure used in the original programming of the game. There are a lot of weird off by 1 errors that are hard to account for in the solver and they were difficult to pin down and solve properly.

If I were to continue working on this project, I would most definitely attempt to go down the path of implementing a couple more board state indicators that I've seen in some other tetris solver implementations. I would then attempt to run a genetic machine learning algorithm against the solver to understand the exact modifiers to maximize board position score for every move to make a solver that can play indefinitely and maximize for tetrises.


## 7. 
The solver is able to play the game consistently assuming it is not given a non-uniform number of random blocks. Essentially, if the solver does not get enough l pieces it won't be able to survive based on the current parameters and vectors for determining score. It is also not able to "spin" pieces at the last minute to fit them into otherwise impossible spots (which players can do, but is actually quite difficult to time for a solver of this nature). The solver will attempt to place blocks in a spot that does not affect the maximum height of the board, does not affect the amount of "holes" in the board, does not create caves/troughs known as board "roughness" and spots that will clear lines. These four characteristics are used to place a best fit position for any given block on the board and are weighted as follows:

```
cleared_lines = 5
max_height = -5
holes = -3
roughness = -0.5
```

Those statistics are then combined to form a score which is maximized across all moves
```
score = cleared_lines + max_height + holes + roughness
```
Note that these parameters are meant to maximize the clearing of lines, and deter creating holes, roughness and a higher overall board. These weights were based off of testing and are definitely not optimized, however they work fairly well.

## 8.
Overall I am happy with the project because it's something I did completely my self and enjoyed the research and trialing to getting a semi-working prototype that could be easily expanded off of to create something a lot better. The solver does play to what I would say is a fairly good standard and while it does from time to time fail fast because of bad luck with blocks if given a decent random uniform set of blocks it performs quite well. 


# Diary

Note: My diary does not have date entries because I can't remember exact when I entered the dates and I started the project a bit later than I liked, so I tended to block off large amounts of time to work on certain pieces and used each block as an entry instead.

### Entry 1 (5 hours)
I attempted to find a simple implementation of tetris so I didn't have to program one manually. I found a tutorial that programs it fairly easily, so I reused the code for the game so I can focus solely on the solver. Full disclosure, the tutorial also has an "AI" implementation in the next article, but I will be writing the implementation myself. I will link references to both the game code and the solver code for full transparency.

My first step is to do a simple heuristic search for placing a block in the "lowest" spot on the board. I think this is a way that most people play naturally when starting off, and I will also NOT rotate pieces and save that for a later step. I need to understand the data structure implementation of the tutorial, so I think just trying to place a non rotated piece in the lowest spot is good for now to make sure I work out all the kinks.




### Entry 2 (2 hours)
I've gotten the non rotated implementation of the game working, and while it doesn't really play the game all that well, it does place pieces with intent to place them in the lowest possible spot. I'm going to implement rotating the pieces, and picking the best spot, with the best rotation. I don't think my piece shifting logic is totally correct, because I seem to run into a couple "off by 1 errors" when moving towards the left, but that only happens when the offset calculation is the very first column and only at the start of the game. I think it has to do with the dimension of pieces, so my offset iteration might have to take that into account. I slightly modified tetris so the blocks will start to drop from the left, instead of from the middle to make my movement calculation easier and made an edge case for when it is at the offset = 0. This did solve my problem, and while I feel like I may have cheated slightly by modifying the game, the solver has in reality unlimited inputs and the game does not progress in speed, so I feel like it's not a big deal.

### Entry 3 (5 hours)
I've managed to get rotations working properly so it will pick a spot with the lowest height for every possible rotation. It does fill the board better, but there are issues with the way in which it fills the board. There are many holes and the machine doesn't actual clear any lines unless it gets lucky. Another heuristic I found from research was "holes" in the board. Combining heuristics can be tricky, so I'm a little hesitant of using both so I might attempt to test the hole heuristic theory instead of the lowest height theory. 

I ended up regressing a bug of not placing pieces properly, as I need to ensure I don't run into index errors when "simulating" piece placement to count empty spaces. An unintended side effect of my changes are that it will never place any blocks in the 10th column, which is an issue obviously. I will be working to fix this small bug and I expect that this will fix a lot of the issues.

I've also read a bit about machine learning theory and if I want to go down the path of multiple heuristics I may want to consider injecting some actual machine learning into the project, assuming I have time. I know that's definitely outside the scope of the class, but it's been something I've been wanting to play with for a while now and it will allow me to finely tune the weighting factors of block height and empty spaces - it might want me to bring in more heuristics, such as continue stacking until a tetris is available. This really isn't required, but it will allow me to play the game the most efficiently in terms of score. 



### Entry 4 (4 hours)
I managed to fix my regression bug so I can actually fill the last column, so the gameplay has improved slightly however without any attention to the filling of holes the gameplay doesn't last very long. 

I am now implementing the empty hole heuristic as part of the calculation for the "best" block placement. I know I will have to weight the empty hole and lowest placement, because technically I could get 4 `I` blocks in a row and lose the game instantly. 

I think I will basically do a "lowest score is best" calculation where height is now `total height - new height` and holes is simple the number of holes created on the entire board if the piece is placed in a certain position. I'll then add the two numbers together (equal weighing) and select the placement with the lowest combined score. 

I'm not sure if this will be the best approach, but it definitely improved the score and longevity comparatively. There are still issues where it doesn't clear blocks when it gets high since it doesn't want to cover a huge hole, but it will actually kill itself due to rather failing than filling a hole, so maybe equal weighing is not the best solution. 

I'm thinking about adding some calculations to do the following
- the lower the board, the more focus on not creating holes and less focus on height
- the higher the board, the more focus on clearing complete rows, more focus on less height

This means I should probably add a heuristic on simulating on how many rows will be cleared if placing a block in a certain position - which is pretty easy to do. 

I'm getting to the point that I've got the base gameplay figured out for the bot, and it needs to be tweaked. I'm really thinking about trying to add some genetic machine learning algorithms to find the perfect weighted ratio of the heuristics, but we'll see if I can tweak the scoring formula a bit more before I move onto that point.


### Entry 5 (2 hours)
After doing a bit more research into other tetris solver implementations I added a roughness quality to move placement, however it tended to not affect results too much. I spent most of my time optimizing and fixing some small bugs as well as finishing the report write up. 



