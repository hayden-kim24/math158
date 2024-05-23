import random
from typing import List
import math
"""
Bonus Question for Pset #6 (due May 22nd!)
Prompt: "Run the Metropolis Algorithm to stimulate the 1-D Ising model with 100 particles.
Return your estimate for the average magnetization at J=1, h=1 and J=5, h=1. 
Submit your code for full credit."
"""

"""
To-do:
1. Define OneDim_Ising class to model an 1D Ising model
2. Define average magnetization function based on metropolis
3. Write stimulation code for average magnetization
"""

"""
References:
"Applied Stochastic Analysis" by Weinan E, Tiejun Li, and Eric Vanden-Eijnden
"Wikipedia - Ising Model" (https://en.wikipedia.org/wiki/Ising_model)
"Wikipedia - Boltzman Constant" (https://simple.wikipedia.org/wiki/Boltzmann_constant)
"""

class OneDim_Ising:
    def __init__(self, numSites,J,h, temp = 5.0):
        #arbitrary temperature value
        self.M = numSites
        self.J = J
        self.h = h
        self.spins = [+1,-1]
        self.x = [random.choice(self.spins) for _ in range(self.M)]
        self.boltzman_constant = 1.3806493*(10^(-23)) #"Wikipedia - Boltzman Constant"
        self.beta = 1/(self.boltzman_constant*temp) #based on p.12 of "Applied Stochastic Analysis"

    #helper function for hamiltonian function
    def sum_adj_mul(self,x:List[int]) -> int:
        result = 0
        for i in range(len(x)-1):
                result += x[i]*x[i+1]
        return result

    #based on the formula provided in p.88 of "Applied Stochastic Analysis"
    def hamiltonian(self, x:List[int]) -> float:
        return -self.J*self.sum_adj_mul(x)-self.h*sum(x)
    
    #based on the formula provided in p.89 of "Applied Stochastic Analysis"
    def magnetization(self, x:List[int]) -> int:
        return sum(x)
    
    #based on the formula provided in p.89 of "Applied Stochastic Analysis"
    def avg_magnetization_metropolis(self) -> float:
        mag_sum = 0
        new_x = self.x.copy()
        for _ in range(1000000):
            #flip the sign for one of the random sites
            new_x[random.choice(range(self.M))] *= -1
            #calculate delta H 
            delta_H = self.hamiltonian(new_x) - self.hamiltonian(self.x)
            #calculate acceptance probability based on p.88 of "Applied Stochastic Analysis"
            a_ij = min(1,math.exp(-self.beta * delta_H))
            #generate a random number based on uniform distribution betwee 0 and 1
            random_num = random.uniform(0,1)
            if random_num <= a_ij:
                self.x = new_x
            #update mag_sum
            mag_sum += (self.magnetization(self.x)/self.M)

        return mag_sum / 1000000

#average magnetization at J=1, h=1
model_one = OneDim_Ising(100,1,1)
print('Model #1: J = 1, h = 1, number of states = 100')
print(f'Average magnetization value after 1000000 iterations:')
print(model_one.avg_magnetization_metropolis())
# average magnetization at J=5, h=1
model_two = OneDim_Ising(100,5,1)
print('Model #2: J = 5, h = 1, number of states = 100')
print(f'Average magnetization value after 1000000 iterations:')
print(model_two.avg_magnetization_metropolis())



    

