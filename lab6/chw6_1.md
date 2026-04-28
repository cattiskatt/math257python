# CHW6.1. A threshold for coordinates: Denoising an audio-signal

CSI Central Illinois is calling. The team recovered an audio recording from a microphone at a crime scene, but there is unfortunately substantial background noise. For their investigation, it is vital to reduce the noise. Can you help the team solve this case?

*Audio signal (plot shown in original prompt)*

The audio signal is a vector in **ℝ¹⁰⁰⁰**. You will convert it into the coordinate system given by the DCT basis. In this coordinate system, each basis element corresponds to a cosine function of a different frequency. Thus, the coordinate vector with respect to the DCT basis tells you how the signal can be written as a linear combination of cosine waves of different frequencies. To eliminate noise, you replace all entries with absolute value smaller than 1 in the coordinate vector by 0. Essentially, you suppress certain frequencies by setting them to 0 (a process from signal processing called *filtering*). Finally, you transfer the new coordinate vector back into the coordinate system given by the standard basis.

The audio recording is given to you as a 1D-numpy array stored in `audio_signal`.

## Tasks

1. Compute the coordinate vector `audio_signal` with respect to the DCT-basis of ℝ¹⁰⁰⁰. Store the coordinate vector as a 1D-numpy array in `coordinates`.

2. Create a new vector obtained from `coordinates` by replacing all entries with absolute value smaller than 1 by 0. Store this new vector as a 1D-numpy array in `coordinates_filtered`.

3. Compute the vector in ℝ¹⁰⁰⁰ whose coordinate vector in the DCT basis is `coordinates_filtered`. Store this vector as a 1D-numpy array in `denoised`.

---

The setup code provides the helper function `create_dct_basis(n)` that creates an *n × n* matrix whose columns make up the *n*-dimensional DCT basis.

## Provided Variables

| Name            | Type         | Description                        |
|-----------------|-------------|------------------------------------|
| `audio_signal`  | numpy array | Audio signal                       |
| `create_dct_basis` | function  | Creates the n-dimensional DCT basis |

## Expected Output Variables

| Name                   | Type         | Description                          |
|------------------------|-------------|--------------------------------------|
| `coordinates`          | numpy array | coordinates in 1000-dimensional DCT basis |
| `coordinates_filtered` | numpy array | new coordinate vector                |
| `denoised`             | numpy array | Denoised audio-signal                |


**Solution**
```python
import numpy as np
n = len(audio_signal) # length of audio signal
dct_matrix = create_dct_basis(n) # creates a DCT basis matrix the size of the lenght of the audio
coordinates = dct_matrix.T @ audio_signal # change of basis to the audio signal
coordinates_filtered = coordinates.copy() # makes a copy to coordinates so nothing within coordinates would be changed
coordinates_filtered[np.abs(coordinates_filtered)<1] =0 # replaces any entires with absolute value that is less than 1, replace with 0
denoised = dct_matrix @ coordinates_filtered # denoised vector, inverse transform

```