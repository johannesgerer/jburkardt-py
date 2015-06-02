#! /usr/bin/env python
#
def poisson ( nrow, ncol ):

#*****************************************************************************80
#
## POISSON returns the POISSON matrix.
#
#  Formula:
#
#    if ( I = J )
#      A(I,J) = 4.0
#    elseif ( I = J+1 or I = J-1 or I = J+NROW or I = J-NROW )
#      A(I,J) = -1.0
#    else
#      A(I,J) = 0.0
#
#  Example:
#
#    NROW = NCOL = 3
#
#     4 -1  0 | -1  0  0 |  0  0  0
#    -1  4 -1 |  0 -1  0 |  0  0  0
#     0 -1  4 |  0  0 -1 |  0  0  0
#     ----------------------------
#    -1  0  0 |  4 -1  0 | -1  0  0
#     0 -1  0 | -1  4 -1 |  0 -1  0
#     0  0 -1 |  0 -1  4 |  0  0 -1
#     ----------------------------
#     0  0  0 | -1  0  0 |  4 -1  0
#     0  0  0 |  0 -1  0 | -1  4 -1
#     0  0  0 |  0  0 -1 |  0 -1  4
#
#  Properties:
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    A is persymmetric: A(I,J) = A(N+1-J,N+1-I).
#
#    A results from discretizing Poisson's equation with the
#    5 point operator on a square mesh of N points.
#
#    A has eigenvalues
#
#      LAMBDA(I,J) = 4 - 2 * COS(I*PI/(N+1))
#                      - 2 * COS(J*PI/(M+1)), I = 1 to N, J = 1 to M.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2015
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
#    Output, real A(NROW*NCOL,NROW*NCOL), the matrix.
#
  import numpy as np

  n = nrow * ncol

  a = np.zeros ( ( n, n ) )

  i = 0

  for i1 in range ( 0, nrow ):
    for j1 in range ( 0, ncol ):

      if ( 0 < i1 ):
        j = i - ncol
        a[i,j] = -1.0

      if ( 0 < j1 ):
        j = i - 1
        a[i,j] = -1.0

      j = i
      a[i,j] = 4.0

      if ( j1 < ncol - 1 ):
        j = i + 1
        a[i,j] = -1.0

      if ( i1 < nrow - 1 ):
        j = i + ncol
        a[i,j] = -1.0

      i = i + 1;

  return a

def poisson_determinant ( nrow, ncol ):

#*****************************************************************************80
#
## POISSON_DETERMINANT returns the determinant of the Poisson matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2015
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
#    Output, real VALUE, the determinant.
#
  import numpy as np

  cr = np.zeros ( nrow )

  for i in range ( 0, nrow ):
    angle = float ( i + 1 ) * np.pi / float ( nrow + 1 )
    cr[i] = np.cos ( angle )

  cc = np.zeros ( ncol )

  for j in range ( 0, ncol ):
    angle = float ( j + 1 ) * np.pi / float ( ncol + 1 )
    cc[j] = np.cos ( angle )

  value = 1.0

  for i in range ( 0, nrow ):
    for j in range ( 0, ncol):
      value = value * ( 4.0 - 2.0 * cr[i] - 2.0 * cc[j] )

  return value

def poisson_determinant_test ( ):

#*****************************************************************************80
#
## POISSON_DETERMINANT_TEST tests POISSON_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print
 
  print ''
  print 'POISSON_DETERMINANT_TEST'
  print '  POISSON_DETERMINANT computes the determinant of the POISSON matrix.'
  print ''

  row_num = 3
  col_num = 3

  m = row_num * col_num
  n = m

  a = poisson ( row_num, col_num )
  r8mat_print ( m, n, a, '  POISSON matrix:' )

  value = poisson_determinant ( row_num, col_num )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'POISSON_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def poisson_rhs ( nrow, ncol, rhs_num ):

#*****************************************************************************80
#
## POISSON_RHS returns the right hand side of a Poisson linear system.
#
#  Discussion:
#
#    The Poisson matrix is associated with an NROW by NCOL rectangular
#    grid of points.
#
#    Assume that the points are numbered from left to right, bottom to top.
#
#    If the K-th point is in row I and column J, set X = I + J.
#
#    This will be the solution to the linear system.
#
#    The right hand side is easily determined from X.  It is 0 for every
#    interior point.
#
#  Example:
#
#    NROW = 3, NCOL = 3
#
#    ^
#    |  7  8  9
#    J  4  5  6
#    |  1  2  3
#    |
#    +-----I---->
#
#    Solution vector X = ( 2, 3, 4, 3, 4, 5, 4, 5, 6 )
#
#    Right hand side B = ( 2, 2, 8, 2, 0, 6, 8, 6, 14 ).
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2015
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
#    Input, integer RHS_NUM, the number of right hand sides.
#
#    Output, real B(NROW*NCOL,RHS_NUM), the right hand side.
#
  import numpy as np

  n = nrow * ncol;

  b = np.zeros ( ( n, 1 ) )

  k = 0

  for i in range ( 0, nrow ):
    for j in range ( 0, ncol ):

      if ( i == 0 ):
        b[k,0] = b[k,0] + i + j + 1

      if ( j == 0 ):
        b[k,0] = b[k,0] + i + j + 1

      if ( j == ncol - 1 ):
        b[k,0] = b[k,0] + i + j + 3

      if ( i == nrow - 1 ):
        b[k,0] = b[k,0] + i + j + 3

      k = k + 1

  return b

def poisson_solution ( nrow, ncol, rhs_num ):

#*****************************************************************************80
#
## POISSON_SOLUTION returns the solution of a Poisson linear system.
#
#  Discussion:
#
#    The Poisson matrix is associated with an NROW by NCOL rectangular
#    grid of points.
#
#    Assume that the points are numbered from left to right, bottom to top.
#
#    If the K-th point is in row I and column J, set X = I + J.
#
#    This will be the solution to the linear system.
#
#  Example:
#
#    NROW = 3, NCOL = 3
#
#    ^
#    |  7  8  9
#    J  4  5  6
#    |  1  2  3
#    |
#    +-----I---->
#
#    Solution vector X = ( 2, 3, 4, 3, 4, 5, 4, 5, 6 )
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2015
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
#    Input, integer RHS_NUM, the number of right hand sides.
#
#    Output, real X(NROW*NCOL,RHS_NUM), the solution.
#
  import numpy as np

  n = nrow * ncol

  x = np.zeros ( ( n, rhs_num ) )

  k = 0
  for i in range ( 0, nrow ):
    for j in range ( 0, ncol ):
      x[k,0] = i + j + 2
      k = k + 1

  return x

def poisson_test ( ):

#*****************************************************************************80
#
## POISSON_TEST tests POISSON.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    05 March 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'POISSON_TEST'
  print '  POISSON computes the POISSON matrix.'

  row_num = 3
  col_num = 3

  m = row_num * col_num
  n = m

  a = poisson ( row_num, col_num )
  r8mat_print ( m, n, a, '  POISSON matrix:' )

  print ''
  print 'POISSON_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  poisson_test ( )
  timestamp ( )
