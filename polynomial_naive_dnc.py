'''
Naive divide and conquer algorithm for polynomial multiplication with theta 0f n as n sqared
'''

import numpy as np


def poly_mult_naive(A, B, n: int, a: int, b: int):
    ''' Recursive implementation to find the product of 2 polynomials '''
    result_array = np.zeros(2*n - 1, dtype=int)
    if n == 1:
        result_array[0] = A[a] * B[b]
        return result_array[0]
    result_array[0:n-1] = poly_mult_naive(A, B, n//2, a, b)
    result_array[n:2*n - 1] = poly_mult_naive(A, B, n//2, a+n//2, b+n//2)
    MN = poly_mult_naive(A, B, n//2, a, b+n//2)
    NM = poly_mult_naive(A, B, n//2, a+n//2, b)
    result_array[(n//2):(3*n // 2) - 1] += MN + NM
    return result_array


def main():
    A = list(
        map(int, input('Enter space separated integer values for polynomial 1').split()))
    B = list(
        map(int, input('Enter space separated integer values for polynomial 2').split()))
    n = max(len(A), len(B))
    a = 0
    b = 0
    print(poly_mult_naive(A, B, max(len(A), len(B)), 0, 0))


main()
