"""
Bonus Question for Pset #6 (due May 22nd!)
Prompt: "Run the Metropolis Algorithm to stimulate the 1-D Ising model with 100 particles.
Return your estimate for the average magnetization at J=1, h=1 and J=5, h=1. 
Submit your code for full credit."
"""

"""
To-do:
1. Define OneDim_Ising class to model an 1D Ising model
2. Define metropolis function
3. Define average magnetization function
3. Write stimulation code for average magnetization
"""

class OneDim_Ising:
    def __init__(self, numParticles,J,h):
        self.numPart = numParticles
        self.J = J
        self.h = h
        self.spins = {+1,-1}

    def adj_mul(x:List[float]) -> List[float]:

    def hamiltonian(self,x:List[float]) -> List[float]:
        return -J*

    
    

