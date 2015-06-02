#!/usr/bin/env python

def nonzeros ( m, n, a ):

#*****************************************************************************80
#
## NONZEROS counts the nonzeros in a matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    31 August 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer M, N, the number of rows and columns.
#
#    Input, real A(M,N), the matrix.
#
#    Output, integer NNZ, the number of nonzero entries.
#
  nnz = 0;
  for j in range ( 0, n ):
    for i in range ( 0, m ):
      if ( a[i,j] != 0.0 ):
        nnz = nnz + 1

  return nnz
