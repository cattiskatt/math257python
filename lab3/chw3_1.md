## CHW 3.1 Matrix Operations: Image Manipulation

You are given an image in the Python variable `image`, which is a `2 x N` matrix of points.

Define two matrix operators: a shear operator and a rotation operator, with details for each given below. Transform the given image with the shear, the rotation, and a combination of the shear then the rotation. Save these as the Python variables `sheared`, `rotated`, and `sheared_and_rotated`.

### Shear operator

Shear mapping is a transformation that moves each point in a direction by an amount that is proportional to its distance to the `x` or `y` axis. You can think of this as “squashing” a figure while maintaining parallel lines along the direction you are shearing.

Create a shear operator that transforms points along the y-axis such that:

```math
x' = x + 0.4y

y' = 0 + y
```

### Rotation operator

The rotation operator transforms points by changing their angle around a point, while keeping the distance constant between each point. You should have seen an example of a rotation transformation in the lab activity.

Create a matrix transformation that rotates `θ = π/6` radians counter-clockwise around the origin. Recall that a rotation can be specified by:

```math
x' = x \,\cos θ - y \,\sin θ

y' = x \,\sin θ + y \,\cos θ
```

The setup code gives the following variables:

| Name | Type | Description |
| --- | --- | --- |
| `image` | numpy array | Image to transform |
| `display_image` | function | Helper function to display an image |

Your code snippet should define the following variables:

| Name | Type | Description |
| --- | --- | --- |
| `sheared` | numpy array | Sheared image |
| `rotated` | numpy array | Rotated image |
| `sheared_and_rotated` | numpy array | Sheared, then rotated image |

### Solution

```python
import numpy as np
import math
theta = pi/6

display_image(image) # diplays original, unmodified image

S = np.array([[1,0.4],[0,1]]) # matrix created given the equation needed to shear the image

sheared = S @ image # applies the operation to the original image, @ means to multiply the two matrix
display_image(sheared) # displayes sheared image

R = np.array([[math.cos(theta),-math.sin(theta)],[math.sin(theta), math.cos(theta)]]) # rotates the image by pi over 6. function is given by the equation above
rotated = R @ image # applies rotation operation to the original matrix
display_image(rotated) # displays roated image

sheared_and_rotated = R @ (S @ image) # multiply by S first to get it sheared, then R to get it rotated
display_image(sheared_and_rotated) # displayed shared and rotated image
```