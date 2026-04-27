Someone in the marketing department multiplied the image of the beloved school logo "I" by a matrix **A**. The result of this operation resulted in the distorted image below, which is storedin the variable `image`.

Luckily we know that the matrix **A** is given as:

Use this information to restore the original image. In the editor box below, write a code snippet that computes the original image, storing it as the variable `corrected`. 

Hint: You can use `np.linalg.inv` to compute the inverse of a matrix. 

```md
The setup code gives the following variables:

| Name          | Type        | Description                    |
|--------------:|:-----------:|:-------------------------------|
| `image`       | numpy array | Distorted image                |
| `display_image` | function   | Helper function to display an image |

Your code snippet should define the following variables:

| Name        | Type        | Description      |
|------------:|:-----------:|:-----------------|
| `corrected` | numpy array | Corrected image  |
```

### Solution 

```python
import numpy as np

A = np.array([[0,3],[2,3]]) # stores the given matrix in A
inv_A = np.linalg.inv(A) # we find the inverse of matrix A
corrected = inv_A @ image # since the original school logo was messed up because we multipled by A, multiplying by the inverse would essentially undo the manipulation, giving us the original logo back

```