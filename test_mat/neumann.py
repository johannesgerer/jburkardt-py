#! /usr/bin/env python
#
def neumann ( nrow, ncol ):

#*****************************************************************************80
#
## NEUMANN returns the NEUMANN matrix.
#
#  Formula:
#
#    I1 = 1 + ( I - 1 ) / NROW
#    I2 = I - ( I1 - 1 ) * NROW
#    J1 = 1 + ( J - 1 ) / NROW
#
#    if ( I = J )
#      A(I,J) = 4
#    elseif ( I = J-1 )
#      If ( I2 = 1 )
#        A(I,J) = -2
#      else
#        A(I,J) = -1
#    elseif ( I = J+1 )
#      If ( I2 = NROW )
#        A(I,J) = -2
#      else
#        A(I,J) = -1
#    elseif ( I = J - NROW )
#      if ( J1 = 2 )
#        A(I,J) = -2
#      else
#        A(I,J) = -1
#    elseif ( I = J + NROW )
#      if ( J1 = NCOL-1 )
#        A(I,J) = -2
#      else
#        A(I,J) = -1
#    else
#      A(I,J) = 0.0
#
#  Example:
#
#    NROW = NCOL = 3
#
#     4 -2  0 | -2  0  0 |  0  0  0
#    -1  4 -1 |  0 -2  0 |  0  0  0
#     0 -2  4 |  0  0 -2 |  0  0  0
#     ----------------------------
#    -1  0  0 |  4 -1  0 | -1  0  0
#     0 -1  0 | -1  4 -1 |  0 -1  0
#     0  0 -1 |  0 -1  4 |  0  0 -1
#     ----------------------------
#     0  0  0 | -2  0  0 |  4 -2  0
#     0  0  0 |  0 -2  0 | -1  4 -1
#     0  0  0 |  0  0 -2 |  0 -2  4
#
#  Properties:
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    A is block tridiagonal.
#
#    A results from discretizing Neumann's equation with the
#    5 point operator on a mesh of NROW by NCOL points.
#
#    A is singular.
#
#    A has the null vector ( 1, 1, ..., 1 ).
#
#    det ( A ) = 0.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Gene Golub, Charles Van Loan,
#    Matrix Computations, second edition,
#    Johns Hopkins University Press, Baltimore, Maryland, 1989
#    (Section 4.5.4).
#
#  Parameters:
#
#    Input, integer NROW, NCOL, the number of rows and columns
#    in the grid.
#
#    Output, integer N, the order of the matrix, which 
#    is NROW*NCOL.
#
#    Output, real A(NROW*NCOL,NROW*NCOL), the NROW*NCOL 
#    by NROW*NCOL matrix.
#
  import numpy as np

  n = nrow * ncol

  a = np.zeros ( ( n, n ) )

  i = 0

  for i1 in range ( 0, nrow ):
    for j1 in range ( 0, ncol ):

      if ( 0 < i1 ):
        j = i - nrow
      else:
        j = i + nrow

      a[i,j] = a[i,j] - 1.0

      if ( 0 < j1 ):
        j = i - 1
      else:
        j = i + 1

      a[i,j] = a[i,j] - 1.0

      j = i
      a[i,j] = 4.0

      if ( j1 < ncol - 1 ):
        j = i + 1
      else:
        j = i - 1

      a[i,j] = a[i,j] - 1.0

      if ( i1 < nrow - 1 ):
        j = i + nrow
      else:
        j = i - nrow

      a[i,j] = a[i,j] - 1.0

      i = i + 1

  return a

def neumann_determinant ( row_num, col_num ):

#*****************************************************************************80
#
## NEUMANN_DETERMINANT returns the determinant of the NEUMANN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer ROW_NUM, COL_NUM, the number of rows and columns in the grid.
#
#    Output, real VALUE, the determinant.
#
  value = 0.0

  return value

def neumann_determinant_test ( ):

#*****************************************************************************80
#
## NEUMANN_DETERMINANT_TEST tests NEUMANN_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
  from neumann import neumann
  from r8mat_print import r8mat_print
 
  print ''
  print 'NEUMANN_DETERMINANT_TEST'
  print '  NEUMANN_DETERMINANT computes the determinant of the NEUMANN matrix.'
  print ''

  row_num = 3
  col_num = 3

  m = row_num * col_num
  n = m

  a = neumann ( row_num, col_num )
  r8mat_print ( m, n, a, '  NEUMANN matrix:' )

  value = neumann_determinant ( row_num, col_num )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'NEUMANN_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def neumann_null_right ( nrow, ncol ):

#*****************************************************************************80
#
## NEUMANN_NULL_RIGHT returns a right null vector of the NEUMANN matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer NROW, NCOL, the number of rows and columns 
#    in the grid.
#
#    Output, real X(NROW*NCOL), the null vector.
#
  import numpy as np

  x = np.ones ( nrow * ncol )
 
  return x

def neumann_test ( ):

#*****************************************************************************80
#
## NEUMANN_TEST tests NEUMANN.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'NEUMANN_TEST'
  print '  NEUMANN computes the NEUMANN matrix.'

  row_num = 3
  col_num = 3

  m = row_num * col_num
  n = m

  a = neumann ( row_num, col_num )
  r8mat_print ( m, n, a, '  NEUMANN matrix:' )

  print ''
  print 'NEUMANN_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  neumann_test ( )
  neumann_determinant_test ( )
  timestamp ( )
