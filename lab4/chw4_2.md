## CHW4.2. Linear Systems: Determining the temperature distribution

In this problem we study the temperature distribution in a two-dimensional object, which we'll model as a grid (see below). Assume that the temperature at the exterior grid points, $S_i$, is constant and known. When the temperature distribution in the grid is stable, the temperature at each interior grid point $T_i$ is the average of the temperatures at the four adjacent points. For example,

```math
T_2 = \frac{T_1 + T_4 + S_7 + S_8}{4}
```

Determine the temperature at the interior points $T_i$ in thermal equilibrium.

![Temperature grid diagram](./temperature_grid.png)

That is, given the vector

```math
\mathbf{S} = \begin{bmatrix} S_0 \\\\ \vdots \\\\ S_8 \end{bmatrix}
```

of the temperatures measured at the boundary grid points, compute the vector

```math
\mathbf{T} = \begin{bmatrix} T_0 \\\\ \vdots \\\\ T_4 \end{bmatrix}
```

of temperatures measured at the interior grid points.

The vector $S$ is stored as a 1-d NumPy array in `s`. Use this to compute `T` and store the vector in `T` as a NumPy array of the same shape as `s`.

The setup code gives the following variables:

| Name | Type | Description |
| --- | --- | --- |
| `s` | numpy array | vector S |

Your code snippet should define the following variables:

| Name | Type | Description |
| --- | --- | --- |
| `T` | numpy array | vector T |

**Note:** The use of `np.linalg.solve()` is not permitted in this equation, as you may not have access to it on the exam. How else can you solve a system of equations?

**Solution**
```python
import numpy as np
```