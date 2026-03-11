import numpy as np

# Function taking as input a terminal price wt = 0 and a maturity time T
# Returns a tuple of 1D arrays for the price and the expected wealth at each time step t from 0 to T-1
def price_return_optimal_price(wt, T):
    # W represents the expected wealth (return)
    W = [wt]
    # P represents the optimal premium (spread)
    P = [wt]
    
    # Market parameters (Liquidity / Elasticity)
    k = 10
    A = 1
    Wprevious = wt
    
    # Backward induction using Bellman equation
    for s in range(1, T + 1):
        # Optimal expected wealth
        Wnew = A * np.exp(-k * (1 / k + Wprevious)) * (1 / k + Wprevious) + (1 - A * np.exp(-k * (1 / k + Wprevious))) * Wprevious
        W.append(Wnew)
        
        # Optimal premium proposed
        Pnew = 1 / k + Wprevious
        P.append(Pnew)

        Wprevious = Wnew
    
    W = np.array(W)
    P = np.array(P)

    # Reverse arrays to get chronological order (t=0 to T)
    W = W[::-1]
    P = P[::-1]

    return P, W

# Test the function
price_return_optimal_price(10**-6, 30)