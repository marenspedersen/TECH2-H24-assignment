"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""
num_list = [1, 2, 3, 4, 5]

def std_loops(x):
    """
    Compute standard deviation of x using loops.

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.

    """

    if len(x) == 0:
        raise ValueError("Cannot compute standard deviation of an empty sequence.")

    # Initialize variables
    n = len(x)
    mean = 0
    variance_sum = 0

    # Calculating the mean
    for num in x:
        mean += num
    mean /= n

    # Calculating the sum of squared differences from the mean
    for num in x:
        variance_sum += (num - mean) ** 2

    # Calculating the variance
    variance = variance_sum / n

    # Calculateing the standard deviation
    sd = variance ** 0.5
    return sd
  

def std_builtin(x, sample=False):
    """
    Compute standard deviation of x using the built-in functions sum()
    and len().

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """

    from math import sqrt
    
    N = len(x)

    # Calculating the mean
    meanVal = sum(x) / N

    # Calculating the sum of squares
    S = sum(num**2 for num in x) / N

    # Calculating the variance
    variance = S - meanVal**2

    # Adjust for sample standard deviation if requested
    if sample:
        variance *= N / (N - 1)  # Use N-1 for sample variance

    # Calculate the standard deviation
    standardDev = sqrt(variance)

    return standardDev



print("Standard Deviation using loops:", std_loops(num_list))
print("Standard Deviation using built-in functions:", std_builtin(num_list))

# Calculate standard deviation using NumPy
import numpy as np
print("Standard Deviation using NumPy:", np.std(num_list))
