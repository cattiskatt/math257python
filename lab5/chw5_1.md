## CHW5.1. So many options: Flying from O'Hare to LAX with at most one layover

Connections between airports can be modelled by a graph. The nodes represent airports, and the edges represent nonstop flight routes between the airports. Two nodes are connected by a edge if there is a nonstop flight between the two airports; for simplicity, we assume that if there is a nonstop flight from one airport to another, there is a returning nonstop flight so that the graph is undirected.

![Airport Network Graph](https://i.imgur.com/your_image_link_here.png)

The matrix `nonstop_flights` represents a network of 100 U.S. airports as described above. We ask you to determine the number of distinct routes to fly from O'Hare Airport (ORD) to Los Angeles International Airport (LAX) with at most one layover (that is, either nonstop or with exactly one layover).

1) Compute a $100 \times 100$-matrix $A$ such that the entry in the $i$-th row and the $j$-th column of $A$ is the number of walks from node $j$ to node $i$ of length at most 2. Store this matrix as `atmost_1_layover`.

2) Assuming that ORD is airport # 26 (the $27^{\text{th}}$ row/column of the adjacency matrix when one-indexing) and LAX is airport # 7 (the $8^{\text{th}}$ row/column of the adjacency matrix when one-indexing). Compute the number of distinct routes to fly from ORD to LAX with at most one layover. Save this as `num_options`.

### The setup code gives the following variables:

| Name | Type | Description |
| :--- | :--- | :--- |
| `nonstop_flights` | numpy array | Network of nonstop flight connections, $100 \times 100$ adjacency matrix |

### Your code snippet should define the following variables:

| Name | Type | Description |
| :--- | :--- | :--- |
| `atmost_1_layover` | numpy array | Network of connections with at most one layover, $100 \times 100$ adjacency matrix |
| `num_options` | integer | Number of routes from ORD to LAX with at most one layover |

**Solution**
```python
import numpy as np

atmost_1_layover = nonstop_flights  + (nonstop_flights @ nonstop_flights) # A = M+ M^2 The fundamental theorem of graph theory in linear algebra states that If M is the adjacency matrix of a grpah, then the entry at (i,j) in the matrix M^k represents the number of walks of length exactly k from node j to i. since we want a length of 2, we would have M^2. M represents walks of length 1, representing nonstop_flights 
# m^2 represents walk of length 2, representing 1-layover flight
# resulting matrix tells you the number of ways to get from any import either using a direct flight or single connection
num_options = atmost_1_layover[26,7] 
# this helps us find the 27th colum and the 8th row. remember that indicies are one less since it starts at 0
```