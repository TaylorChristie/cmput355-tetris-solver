## Question Responses
1. tsc2
2. Taylor Christie 1528468 tsc2
3. Well, I did the entire project myself with no external help (other than some research and a previously programmed version of the game so I didn't have to write it myself). I feel like I performed to my expectations in this project :)
4. https://github.com/TaylorChristie/cmput355-tetris-solver
5. The game I decided to write a solver for is tetris. Basically, the object of the game is to stack 7 different types of randomly generated blocks together to obtain points and stay alive as long as possible.
6. 1/2 page summary of what you accomplished for the project. What were your original goals? did you achieve some/all of them? what was the most satisfying part? What was the most dissapointing part? if you continue to work on this project later what else would you like to do?
7. Include data that measures the performance of your project: as a solver describe what problems it can solve and what it can't. 


## Diary

I picked this project because I wanted to build something that seemed algorithmically simple but was difficult to implement. It has straightforward rules, but a huge variety of ways to play the game effectively. This game does not require a super computer to play either, but it requires clever intuition to program it to work well and requires some math.

### Entry 1
I attempted to find a simple implementation of tetris so I didn't have to program one manually. I found a tutorial that programs it fairly easily, so I reused the code for the game so I can focus solely on the solver. Full disclosure, the tutorial also has an "AI" implementation in the next article, but I will be writing the implementation myself. I will link references to both the game code and the solver code for full transparency.

My first step is to do a simple hueristic search for placing a block in the "lowest" spot on the board. I think this is a way that most people play naturally when starting off, and I will also NOT rotate pieces and save that for a later step. I need to understand the data structure implementation of the tutorial, so I think just trying to place a non rotated piece in the lowest spot is good for now to make sure I work out all the kinks.




### Entry 2
I've gotten the non rotated implementation of the game working, and while it doesn't really play the game all that well, it does place peices with intent to place them in the lowest possible spot. I'm going to implement rotating the peices, and picking the best spot, with the best rotation. I don't think my peice shifting logic is totally correct, because I seem to run into a couple "off by 1 errors" when moving towards the left, but that only happens when the offset calculation is the very first column and only at the start of the game. I think it has to do with the dimension of peices, so my offset iteration might have to take that into account. I slightly modified tetris so the blocks will start to drop from the left, instead of from the middle to make my movement calculation easier and made an edge case for when it is at the offset = 0. This did solve my problem, and while I feel like I may have cheated slightly by modifying the game, the solver has in reality unlimited inputs and the game does not progress in speed, so I feel like it's not a big deal.

### Entry 3
I've managed to get rotations working properly so it will pick a spot with the lowest height for every possible rotation. It does fill the board better, but there are issues with the way in which it fills the board. There are many holes and the machine doesn't actual clear any lines unless it gets lucky. Another heuristic I found from research was "holes" in the board. Combining heuristics can be tricky, so I'm a little hesitant of using both so I might attempt to test the hole heuristic theory instead of the lowest height theory. 

I ended up regressing a bug of not placing pieces properly, as I need to ensure I don't run into index errors when "simulating" piece placement to count empty spaces. An unintended side effect of my changes are that it will never place any blocks in the 10th column, which is an issue obviously. I will be working to fix this small bug and I expect that this will fix a lot of the issues.

I've also read a bit about machine learning theory and if I want to go down the path of multiple heuristics I may want to consider injecting some actual machine learning into the project, assuming I have time. I know that's definitely outside the scope of the class, but it's been something I've been wanting to play with for a while now and it will allow me to finely tune the weighting factors of block height and empty spaces - it might want me to bring in more heuristics, such as continue stacking until a tetris is available. This really isn't required, but it will allow me to play the game the most effeciently in terms of score. 



### Entry 4
I managed to fix my regression bug so I can actually fill the last column, so the gameplay has improved slightly however without any attention to the filling of holes the gameplay doesn't last very long. 

I am now implementing the empty hole heuristic as part of the calculation for the "best" block placement. I know I will have to weight the empty hole and lowest placement, because technically I could get 4 `I` blocks in a row and lose the game instantly. 

I think I will basically do a "lowest score is best" calculation where height is now `total height - new height` and holes is simple the number of holes created on the entire board if the piece is placed in a certain position. I'll then add the two numbers together (equal weighing) and select the placement with the lowest combined score. 

I'm not sure if this will be the best approach, but it definitely improved the score and longevity comparitively. There are still issues where it doesn't clear blocks when it gets high since it doesn't want to cover a huge hole, but it will actually kill itself due to rather failing than filling a hole, so maybe equal weighing is not the best solution. 

I'm thinking about adding some calculations to do the following
- the lower the board, the more focus on not creating holes and less focus on height
- the higher the board, the more focus on clearing complete rows, more focus on less height

This means I should probably add a heuristic on simulating on how many rows will be cleared if placing a block in a certain position - which is pretty easy to do. 

I'm getting to the point that I've got the base gameplay figured out for the bot, and it needs to be tweaked. I'm really thinking about trying to add some genentic machine learning algorithms to find the perfect weighted ratio of the hueristics, but we'll see if I can tweak the scoring formula a bit more before I move onto that point.


### Entry 5




