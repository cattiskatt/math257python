import numpy as np

def investment(p1,p2,p3,assets,t):
    p1t, p2t, p3t = assets # define the assets as a tuple
    value = p1[t]*p1t + p2[t]*p2t + p3[t]*p3t # linear combination to find the value our investment
    return value # return the value of the investment 