# DCT Image Compression with Chunking

The discrete cosine transform is a powerful technique for expressing data as a sum of cosine waves, and has many applications in audio and image compression. We will use the "chunking" technique discussed in the lab activity here to compress a whole image.

*Image (shown in original prompt)*

Given a **512 × 512** image, stored in the variable `image`, you will break the image into smaller **8 × 8** chunks. Then for each chunk, you will convert to the DCT basis, drop the frequencies with relatively small contribution, then convert back to the standard basis and clip the resulting pixel values so that they lie between 0 and 255. This image is given in gray scale, where each pixel varies from 0 to 255. To gauge which frequencies have a small contribution, use a tolerance of **10% of the largest absolute value** in each particular chunk after converting it into the DCT basis.

The setup code provides the helper function `create_dct_basis(n)`, which creates an **n × n** matrix whose columns make up the *n*-dimensional DCT basis.

## Tasks

To construct your solution, write a code snippet that:

- Defines the function `compress_chunk(chunk)` that takes as argument a "chunk" of the image, with dimension **8 × 8**, and returns the compressed "chunk".
- Make sure your compressed chunk returned from `compress_chunk()` contains only values between **0 and 255**, as in the original image. You may find the function `numpy.clip()` useful.
- Use your function to construct the variable `compressed`, which contains the compressed `image`.

---

## Provided Variables

| Name               | Type                | Description                  |
|--------------------|---------------------|------------------------------|
| `image`            | 512 × 512 numpy array | Test image                   |
| `create_dct_basis` | function            | Creates the n-dimensional DCT basis |

## Expected Output Variables

| Name             | Type                | Description                          |
|------------------|---------------------|--------------------------------------|
| `compress_chunk` | function            | Function to compress an 8 × 8 chunk  |
| `compressed`     | 512 × 512 numpy array | Compressed image                    |


**Solution**
```python
import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

D = create_dct_basis(8) # creates a dct basis matrix of size 8, as we are trying to break the image into size 8

def compress_chunk(chunk):
    Y = D.T @ chunk @ D #An 8x8 matrix of "DCT coefficients." The top-left value usually represents the average brightness of the block, while the other values represent how much high-frequency detail (edges, textures) is in that block.
    tolerance = 0.10 * np.max(np.abs(Y)) # looks at the strongest frqeunecy
    
    Y_filtered = Y.copy()
    Y_filtered[np.abs(Y_filtered) < tolerance] = 0 # anything less than the tolerance is set to 0
    
    compress_reconstructed = D @ Y_filtered @ D.T # transforms the data back
    return np.clip(compress_reconstructed, 0, 255) # pixesl must be within a certain range
    
compressed = np.zeros_like(image) # emty matrix with size of 512 x 512
height,width = image.shape # assigns 512 to both height and width

for i in range(0, height, 8):
    for j in range(0,width,8):
        current_chunk = image[i:i+8, j:j+8] # splicing each chunck
        compressed[i:i+8, j:j+8] = compress_chunk(current_chunk) # after splicing each specific chunk, compress that respective chunk using the compress chunk function and store that within the empty matrix we created earlier

```