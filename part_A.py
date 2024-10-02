"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""
values = [1, 2, 3, 4, 5, 3, 54, 64, 645]

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

    # Step 1: Initialize variables
    n = len(x)
    mean = 0.0
    variance_sum = 0.0

    # Step 2: Calculate the mean using a loop
    for num in x:
        mean += num
    mean /= n

    # Step 3: Calculate the sum of squared differences from the mean
    for num in x:
        variance_sum += (num - mean) ** 2

    # Step 4: Calculate the variance (population)
    variance = variance_sum / n

    # Step 5: Calculate the standard deviation
    sd = variance ** 0.5
    return sd

def std_builtin(x):
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

    N = len(values)

    # Calculate the mean
    meanVal = sum(values) / N

    # Calculate the sum of squares (S)
    S = sum(x**2 for x in values) / N

    # Calculate the variance
    variance = S - meanVal**2

    # Calculate the standard deviation
    standardDev = sqrt(variance)

    print(standardDev)

    import numpy as np

    # Calculate standard deviation
    std_dev = np.std(values)

    print("Standard Deviation:", std_dev)


import numpy as np

# Calculate standard deviation
std_dev = np.std(values)

print("Standard Deviation:", std_dev)
    