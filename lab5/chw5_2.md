# CHW5.2. Graphs: Meme spread in social networks

Graphs can be used in mathematics and other fields to represent objects and the connections between them. Here, we will use a directed graph to represent people in a social network and their friend connections with one another. In this directed graph nodes correspond to people. An edge between two nodes indicates friendship between the corresponding people. The direction of the edge is chosen at random and carries no further meaning. A friend group is a *connected component* of this graph. We will use this to model the spread of a meme throughout this social network.

We give you the edge-node incidence matrix of this graph. It is stored as a 2D-numpy array `friends`.

1. Find the number of friend groups of this network. Store this value as `num_friend_groups`.  
   This should be the number of connected components in this directed graph.

2. Assuming that a meme originates at person 113 (assume zero-indexing), find the number of people that will see the meme (including the original person).  
   Assume each person will send the meme to all of their friends. Save this as `num_meme_spread`.

We also give you a function `nullspace`. Given a matrix as a 2D-numpy array of shape `(m,n)`, this function will return an 2D-numpy array of shape `(n,d)` consisting of a basis of the nullspace of the original matrix.


The setup code gives the following variables:

| Name        | Type        | Description                    |
|-------------|------------|--------------------------------|
| `friends`   | numpy array | edge-node incidence matrix     |
| `nullspace` | function    | returns basis of nullspace of a matrix |


Your code snippet should define the following variables:

| Name                | Type    | Description                              |
|---------------------|---------|------------------------------------------|
| `num_friend_groups` | integer | Number of overall friend groups          |
| `num_meme_spread`   | integer | Number of people that will receive the meme |

**Solution**
```python
import numpy as np

num_nodes = nullspace(friends) # returns the basis of nullspace of matrix friends
num_friend_groups = num_nodes.shape[1] # number of friend group is determined by the number of nodes
group = np.argmax(np.abs(num_nodes[113,:])) # looks for the person at index 113, np.abs is used as a node will have a non-zero value only in the column (basis vector) corresponding to its own connected componen,argmax finds which "group vector" person 113 belongs to.

mem = np.abs(num_nodes[:, group]) # extracts the entire group based on the meme spread
num_meme_spread = np.sum(mem) #sum of all the people who spread the meme

```