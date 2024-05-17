import numpy as np

class RandomWalk:
    """
    RandomWalk generates a discrete random walk
    """
    def __init__(self, probabilities, possible_steps, steps_so_far = 0):
        #list of probabilities for each possible step
        # the sum of all elements must be 1
        # ex = [1/2,1/2]
        self.probabilities = probabilities
        # list of possible steps
        # ex = [+1, -1]
        self.possible_steps = possible_steps
        # keeps track of the number of steps taken so far 
        # integer value
        self.steps_so_far = steps_so_far
    
    def generate_step(self):
        """
         Generate a random step based on the self.possible_steps
        """
        return np.random.choice(self.possible_steps, replace = True,p = self.probabilities)

    def generate_walk(self,total_number_of_steps):
         """
         Generate a walk with a certain number of steps.
         Will return a list of what type of step was taken.
        """
         self.steps_so_far += total_number_of_steps
         return [self.generate_step() for _ in range(total_number_of_steps)]
    

#example: the most basic random walk
probabilities_ex = [1/2,1/2]
possible_steps_ex = [+1,-1]
rw_ex = RandomWalk(probabilities_ex,possible_steps_ex)
print(rw_ex.generate_step())
print(rw_ex.generate_walk(10))

#another example: random walk with N, S, W, E
probabilities_ex_2 = [1/4,1/4,1/4,1/4]
possible_steps_ex_2 = ["N","S","W","E"]
rw_ex_2 = RandomWalk(probabilities_ex_2,possible_steps_ex_2)
print(rw_ex_2.generate_step())
print(rw_ex_2.generate_walk(10))