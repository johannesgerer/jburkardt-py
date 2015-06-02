#! /usr/bin/env python
#
def wilson ( ):

#*****************************************************************************80
#
## WILSON returns the Wilson matrix.
#
#  Formula:
#
#    A =
#     5  7  6  5
#     7 10  8  7
#     6  8 10  9
#     5  7  9 10
#
#  Properties:
#
#    The Higham/MATLAB version of this matrix has rows and columns
#    1 and 2 interchanged.
#
#    A is symmetric: A' = A.
#
#    Because A is symmetric, it is normal.
#
#    Because A is normal, it is diagonalizable.
#
#    A is positive definite.
#
#    det ( A ) = 1.
#
#    A is ill-conditioned.
#
#    A * X = B, where X is the Wilson solution vector, and B is the
#    Wilson right hand side.
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joan Westlake,
#    A Handbook of Numerical Matrix Inversion and Solution of 
#    Linear Equations,
#    John Wiley, 1968,
#    ISBN13: 978-0471936756,
#    LC: QA263.W47.
#
#  Parameters:
#
#    Output, real A(4,4), the matrix.
#
  import numpy as np

  a = np.array ( [ \
    [ 5.0,  7.0,  6.0,  5.0 ], \
    [ 7.0, 10.0,  8.0,  7.0 ], \
    [ 6.0,  8.0, 10.0,  9.0 ], \
    [ 5.0,  7.0,  9.0, 10.0 ] ] )

  return a

def wilson_condition ( ):

#*****************************************************************************80
#
## WILSON_CONDITION returns the L1 condition of the WILSON matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    22 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real COND, the L1 condition number.
#
  cond = 4488.0

  return cond

def wilson_condition_test ( ):

#*****************************************************************************80
#
## WILSON_CONDITION_TEST tests WILSON_CONDITION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 December 2014
#
#  Author:
#
#    John Burkardt
#
  from wilson import wilson
  from r8mat_print import r8mat_print

  print ''
  print 'WILSON_CONDITION_TEST'
  print '  WILSON_CONDITION computes the condition of the WILSON matrix.'
  print ''

  n = 4
  a = wilson ( )
  r8mat_print ( n, n, a, '  WILSON matrix:' )

  value = wilson_condition ( )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'WILSON_CONDITION_TEST'
  print '  Normal end of execution.'

  return

def wilson_determinant ( ):

#*****************************************************************************80
#
## WILSON_DETERMINANT returns the determinant of the WILSON matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#
#    Output, real VALUE, the determinant.
#
  value = 1.0

  return value

def wilson_determinant_test ( ):

#*****************************************************************************80
#
## WILSON_DETERMINANT_TEST tests WILSON_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 February 2015
#
#  Author:
#
#    John Burkardt
#
  from wilson import wilson
  from r8mat_print import r8mat_print

  print ''
  print 'WILSON_DETERMINANT_TEST'
  print '  WILSON_DETERMINANT computes the determinant of the WILSON matrix.'
  print ''

  n = 4
  a = wilson ( )
  r8mat_print ( n, n, a, '  WILSON matrix:' )

  value = wilson_determinant ( )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'WILSON_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def wilson_eigen_right ( ):

#*****************************************************************************80
#
## WILSON_EIGEN_RIGHT returns the right eigenvectors of the WILSON matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real A(4,4), the right eigenvector matrix.
#
  import numpy as np
#
#  Note that the matrix entries are listed by row.
#
  a = np.array ( [ \
   [ 0.380262074390714,   \
     0.396305561186082,   \
     0.093305039089285,   \
     0.830443752841578 ], \
   [ 0.528567849528642,   \
     0.614861280394151,   \
    -0.301652326903523,   \
    -0.501565058582058 ], \
   [ 0.551954849631663,   \
    -0.271601039711768,   \
     0.760318430013036,   \
    -0.208553600252039 ], \
   [ 0.520924780743657,   \
    -0.625396181050490,   \
    -0.567640668325261,   \
     0.123697458332363 ] ] )

  return a

def wilson_eigenvalues ( ):

#*****************************************************************************80
#
## WILSON_EIGENVALUES returns the eigenvalues of the WILSON matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real LAM(4), the eigenvalues..
#
  import numpy as np

  lam = np.array ( [ \
    [ 30.288685345802129 ], \
    [  3.858057455944950 ], \
    [  0.843107149855033 ], \
    [  0.010150048397892 ] ] )

  return lam

def wilson_inverse ( ):

#*****************************************************************************80
#
## WILSON_INVERSE returns the inverse of the Wilson matrix.
#
#  Formula:
#
#     68 -41 -17  10
#    -41  25  10  -6
#    -17  10   5  -3
#     10  -6  -3   2
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
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    18 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Joan Westlake,
#    A Handbook of Numerical Matrix Inversion and Solution of 
#    Linear Equations,
#    John Wiley, 1968,
#    ISBN13: 978-0471936756,
#    LC: QA263.W47.
#
#  Parameters:
#
#    Output, real A(4,4), the matrix.
#
  import numpy as np
#
#  Note that the matrix entries are listed by row.
#
  a = np.array ( [ \
    [  68.0, -41.0, -17.0,  10.0 ], \
    [ -41.0,  25.0,  10.0,  -6.0 ], \
    [ -17.0,  10.0,   5.0,  -3.0 ], \
    [  10.0,  -6.0,  -3.0,   2.0 ] ] )

  return a

def wilson_llt ( ):

#*****************************************************************************80
#
## WILSON_LLT returns the lower triangular Cholesky factor of the WILSON matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    15 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real A(4,4), the matrix.
#
  import numpy as np
#
#  Note that the matrix entries are listed by row.
#
  a = np.array ( [ \
  [ 2.236067977499790,  0.0,                 \
    0.0,                0.0               ], \
  [ 3.130495168499706,  0.447213595499957,   \
    0.0,                0.0               ], \
  [ 2.683281572999748, -0.894427190999918,   \
    1.414213562373093,  0.0               ], \
  [ 2.236067977499790,  0.0,                 \
    2.121320343559645,  0.707106781186539 ] ] )

  return a

def wilson_plu ( ):

#*****************************************************************************80
#
## WILSON_PLU returns the PLU factors of the WILSON matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, P(4,4), L(4,4), U(4,4), the PLU factors.
#
  import numpy as np

  p = np.array ( [ \
    [ 0.0,  0.0,  0.0,  1.0 ], \
    [ 1.0,  0.0,  0.0,  0.0 ], \
    [ 0.0,  1.0,  0.0,  0.0 ], \
    [ 0.0,  0.0,  1.0,  0.0 ] ] )

  l = np.array ( [ \
   [ 1.0,                0.00,  0.00,  0.00 ], \
   [ 0.857142857142857,  1.00,  0.00,  0.00 ], \
   [ 0.714285714285714,  0.25,  1.00,  0.00 ], \
   [ 0.714285714285714,  0.25, -0.20,  1.00 ] ] )

  u = np.array ( [ \
    [ 7.00, 10.0,               8.0,               7.00 ], \
    [ 0.00, -0.571428571428571, 3.142857142857143, 3.00 ], \
    [ 0.00,  0.0,               2.50,              4.25 ], \
    [ 0.00,  0.0,               0.0,               0.10 ] ] )

  return p, l,  u

def wilson_rhs ( ):

#*****************************************************************************80
#
## WILSON_RHS returns the WILSON right hand side.
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
#    Output, real B(4,1), the right hand side vector.
#
  import numpy as np

  b = np.array ( [ [ 23.0 ], [ 32.0 ], [ 33.0 ], [ 31.0 ] ] )

  return b

def wilson_solution ( ):

#*****************************************************************************80
#
## WILSON_SOLUTION returns the WILSON solution.
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
#    Output, real X(4,1), the solution vector.
#
  import numpy as np

  x = np.array ( [ [ 1.0 ], [ 1.0 ], [ 1.0 ], [ 1.0 ] ] )

  return x

def wilson_test ( ):

#*****************************************************************************80
#
## WILSON_TEST tests WILSON.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    20 December 2014
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'WILSON_TEST'
  print '  WILSON computes the WILSON matrix.'

  n = 4
  a = wilson ( )
  r8mat_print ( n, n, a, '  WILSON matrix:' )

  print ''
  print 'WILSON_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  wilson_test ( )
  timestamp ( )
