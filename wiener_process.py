import numpy as np

class Wiener_Process:
    """
    For Week 7 and 8, we learned about Wiener Process (also known as Brownian Motion).
    """
    def __init__(self,initial_value: float = 0.0, time_interval: Tuple[float,float] = (0.0, 1.0), variance: float = 1.0):
        self.initial_value = initial_value
        self.time_interval = time_interval
        self.variance = variance
    

    def samples_karhunen_loeve(self, t_points: int, n_terms: int):
         """
         Based on Week 8 Monday Lecture for Math 158 (05/20/24):
         We can sample and approximate Wiener Process(Brownian Motion) by calculating the first few terms of Kahunen Loeve Expansion.
         For KL Expansion, we are taking advantage of the eigenvalues and the eigenfunctions that we derived in class for the covariance operator.
         
         Parameters: 
         t_points: number of time points for discretizing time
         n_terms: number of terms we are using from the K-L expansion
         m_samples: number of samples we are generating
         """

        self.time_list = np.linspace(self.time_interval[0], self.time_interval[1],t_points)
        phi = 
        

    