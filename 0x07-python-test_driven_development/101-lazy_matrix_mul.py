#!/usr/bin/python3
"""
Multiply two matrix elements


Always Success

"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return a multiply of two matrix"""

    result = np.matmul(m_a, m_b)
    return result
