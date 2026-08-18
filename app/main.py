import numpy as np


def calculate_statistics(matrix: np.ndarray) -> dict:
    return {
        "mean": np.mean(matrix),
        "median": np.median(matrix),
        "std": np.std(matrix),
        "sum": np.sum(matrix)
    }

