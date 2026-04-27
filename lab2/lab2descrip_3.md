## CHW2.3. Computing the value of your investment

This question is a generalization of the previous question that you completed using the workspace. Note that the two questions are independent, and any of the variables defined before will not be carried over (this is the case for ALL PrairieLearn questions due to the way the system is designed).

Use the knowledge that you obtained in the previous question to write a function with the following signature:

```python
def investment(p1, p2, p3, assets, t):
    """Return the total investment value at time t."""
    return p1[t] * assets[0] + p2[t] * assets[1] + p3[t] * assets[2]
```

Your code snippet needs to define the function `investment` that will take as arguments three 1d numpy arrays `p1`, `p2` and `p3` with same size, a tuple `assets` and an integer `t`. 

The numpy arrays contain the history of stock prices for the three companies. 

The tuple `assets` has three entries, where each entry corresponds to the number of assets for the companies with stock prices `p1`, `p2` and `p3` respectively.

The integer `t` is the time where we want you to compute the value of your investment which will be the output of the function `investment`. The variable `t` varies from `0` to `len(p1)-1`.
