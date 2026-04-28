# CHW7.1 Markov matrices: GoT meets 538

On the fictional island of Westeros, the four great houses (House Targaryen, House Stark, House Baratheon and House Lannister) are in an eternal power struggle for the Iron Throne. You are working for the Westeros-equivalent of FiveThirtyEight, and it is your task to determine for each house the long term probability that one of their members sits on the Iron Throne. Nate Silver already told you that the transition probabilities from one year to the next are given by the following Markov chain:

*(diagram shown in original problem)*

1) Compute the 4 × 4-matrix transition matrix T for the above Markov chain. Sort the columns as follows: House Targaryen, House Stark, House Baratheon, and House Lannister. Store this matrix as `markov_matrix`.

2) Compute the steady state vector of this system, that is, find a probability vector which is an eigenvector of T with eigenvalue 1. Save this as `steady_state`.

3) Suppose a member of House Targaryen currently sits on the Iron Throne. What is the probability that a member of House Stark sits on the throne in exactly three years? Save this as `prob_stark`.

---

Your code snippet should define the following variables:

| Name           | Type         | Description        |
|----------------|--------------|--------------------|
| `markov_matrix` | numpy array  | Transition matrix   |
| `steady_state`  | numpy array  | Steady state vector|
| `prob_stark`    | float        | Probability        |


**Solution**
```python
import numpy as np

# 1. Compute the transition matrix
# Order: House Targaryen, House Stark, House Baratheon, House Lannister
# Columns represent the "from" state, rows represent the "to" state
markov_matrix = np.array([
    [0.80,  0.10,  0.050, 0.10], # To Targaryen
    [0.010, 0.50,  0.10,  0.10], # To Stark
    [0.050, 0.10,  0.75,  0.10], # To Baratheon
    [0.14,  0.30,  0.10,  0.70]  # To Lannister
])

# 2. Compute the steady state vector
# Calculate eigenvalues and right eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(markov_matrix)

# Find the index of the eigenvalue that is equal to 1 
# (using argmin and abs to handle slight floating-point inaccuracies)
steady_state_index = np.argmin(np.abs(eigenvalues - 1.0))

# Extract the eigenvector corresponding to eigenvalue 1
steady_state_unnormalized = np.real(eigenvectors[:, steady_state_index])

# Normalize the eigenvector so its components sum to 1 (probability vector)
steady_state = steady_state_unnormalized / np.sum(steady_state_unnormalized)

# 3. Compute probability Stark sits on throne in 3 years given Targaryen sits now
# Initial state vector for Targaryen
v_0 = np.array([1.0, 0.0, 0.0, 0.0])

# Calculate the state after 3 years: v_3 = (T^3) * v_0
T_cubed = np.linalg.matrix_power(markov_matrix, 3)
v_3 = T_cubed @ v_0

# The probability of Stark is at index 1 of the resulting vector
prob_stark = v_3[1]

```