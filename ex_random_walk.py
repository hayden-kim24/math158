import random_walk

#example: the most basic random walk
probabilities_ex = [1/2,1/2]
possible_steps_ex = [+1,-1]
rw_ex = random_walk.RandomWalk(probabilities_ex,possible_steps_ex)
print(rw_ex.generate_step())
print(rw_ex.generate_walk(10))

#another example: random walk with N, S, W, E
probabilities_ex_2 = [1/4,1/4,1/4,1/4]
possible_steps_ex_2 = ["N","S","W","E"]
rw_ex_2 = random_walk.RandomWalk(probabilities_ex_2,possible_steps_ex_2)
print(rw_ex_2.generate_step())
print(rw_ex_2.generate_walk(10))