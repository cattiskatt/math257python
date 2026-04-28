# Six Degrees of Separation

It's said that everyone in the world is connected to each other by at most six degrees of separation. For example, you know someone who knows someone who knows someone who knows someone who knows someone who knows someone who knows the president of the United States. Of course, this can never be truly tested, but scientists and mathematicians estimate that it could be much less. A study found that Twitter users are on average connected to each other through a chain of at most 4 people.

You will write a function which checks whether or not every pair of people from a group is connected by **at most** a certain degree of separation.

Your function should take in a graph (as an adjacency matrix) and a distance and should then return `True` if every pair of nodes is connected by a walk of **at most** the specified distance, and `False` otherwise.

## Hints

- `np.all(matrix > 0)` will return `True` if all of the entries of `matrix` are positive and `False` otherwise.
- `la.matrix_power(M, n)` will return the `n`-th power of `M`.
- What do the entries on the diagonal of an adjacency matrix represent? How do their values relate to the problem?

**Solution**
```python
import numpy as np
import numpy.linalg as la

def connected(network, degree):
    num_nodes = network.shape[1] # num of nodes of graph related matrix can be found by taking the shape of it
    M = network + np.eye(num_nodes) #Adds 1s to the diagonal. This ensures that when we calculate powers, we include paths that are shorter than the maximum degree.
    M_powered = la.matrix_power(M, degree) #Raises the modified matrix to the power of the degree. If the degree is 6, this calculates all connections reachable in 6 steps or fewer.
    return np.all(M_powered > 0) #Checks if every single entry in the resulting matrix is greater than 0. If there is even one 0, it means those two people are not connected within that distance.

```