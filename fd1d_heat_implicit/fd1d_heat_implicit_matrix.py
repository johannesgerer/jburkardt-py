#! /usr/bin/env python
#
def fd1d_heat_implicit_matrix ( x_num, cfl ):

#*****************************************************************************80
#
## FD1D_HEAT_IMPLICIT_MATRIX: set the system matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 January 2012
#
#  Author:
#
#    John Burkardt
#
  import numpy as np

  a = np.zeros ( ( x_num, x_num ) )

  a[0,0] = 1.0

  for i in range ( 1, x_num - 1 ):
    a[i,i-1] =           - cfl
    a[i,i  ] = 1.0 + 2.0 * cfl
    a[i,i+1] =           - cfl

  a[x_num-1,x_num-1] = 1.0

  return a

