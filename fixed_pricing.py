import numpy as np

# Function taking as input a terminal price wt = 0 and a maturity time T
# Returns a tuple of 1D arrays for the price and the expected wealth at each time step t using a FIXED premium
def price_return_fixe_price(wt, T):
    # W represents the expected wealth (return)
    W = [wt]
    # P represents the premium (spread)
    P = [wt]
    
    # Market parameters
    k = 10
    A = 1
    Wprevious = wt
    
    # Backward induction using Bellman equation with a constant premium of 0.45
    for s in range(1, T + 1):
        Wnew = A * np.exp(-k * 0.45) * 0.45 + (1 - A * np.exp(-k * 0.45)) * Wprevious
        W.append(Wnew)

        Pnew = 0.45
        P.append(Pnew)

        Wprevious = Wnew

    W = np.array(W)
    P = np.array(P)

    # Reverse arrays to get chronological order (t=0 to T)
    W = W[::-1]
    P = P[::-1]

    return P, W

# Test the function
price_return_fixe_price(10**-6, 30)