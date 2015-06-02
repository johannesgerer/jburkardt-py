#! /usr/bin/env python
#
def kershaw ( ):

#*****************************************************************************80
#
## KERSHAW returns the KERSHAW matrix.
#
#  Discussion:
#
#    The Kershaw matrix is a simple example of a symmetric
#    positive definite matrix for which the incomplete Cholesky
#    factorization fails, because of a negative pivot.
#
#  Example:
#
#     3 -2  0  2
#    -2  3 -2  0
#     0 -2  3 -2
#     2  0 -2  3
#
#  Properties:
#
#    A is symmetric.
#
#    A is positive definite.
#
#    det ( A ) = 1.
#
#    LAMBDA(A) = [ 
#      5.828427124746192
#      5.828427124746188
#      0.171572875253810
#      0.171572875253810 ].
#
#    A does not have an incompete Cholesky factorization.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
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

  a = np.array ( [ \
    [  3.0, -2.0,  0.0,  2.0 ], \
    [ -2.0,  3.0, -2.0,  0.0 ], \
    [  0.0, -2.0,  3.0, -2.0 ], \
    [  2.0,  0.0, -2.0,  3.0 ] ] )

  return a

def kershaw_condition ( ):

#*****************************************************************************80
#
## KERSHAW_CONDITION returns the L1 condition of the KERSHAW matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VALUE, the condition.
#
  a_norm = 7.0
  b_norm = 7.0
  value = a_norm * b_norm

  return value

def kershaw_condition_test ( ):

#*****************************************************************************80
#
## KERSHAW_CONDITION_TEST tests KERSHAW_CONDITION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
  from kershaw import kershaw
  from r8mat_print import r8mat_print

  print ''
  print 'KERSHAW_CONDITION_TEST'
  print '  KERSHAW_CONDITION computes the condition of the KERSHAW matrix.'
  print ''

  n = 4
  a = kershaw ( )
  r8mat_print ( n, n, a, '  KERSHAW matrix:' )

  value = kershaw_condition ( )
  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'KERSHAW_CONDITION_TEST'
  print '  Normal end of execution.'

  return

def kershaw_determinant ( ):

#*****************************************************************************80
#
## KERSHAW_DETERMINANT returns the determinant of the KERSHAW matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VALUE, the determinant.
#
  value = 1.0

  return value

def kershaw_determinant_test ( ):

#*****************************************************************************80
#
## KERSHAW_DETERMINANT_TEST tests KERSHAW_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
  from kershaw import kershaw
  from r8mat_print import r8mat_print

  print ''
  print 'KERSHAW_DETERMINANT_TEST'
  print '  KERSHAW_DETERMINANT computes the determinant of the KERSHAW matrix.'
  print ''

  n = 4
  a = kershaw ( )
  r8mat_print ( n, n, a, '  KERSHAW matrix:' )

  value = kershaw_determinant ( )
  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'KERSHAW_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def kershaw_eigen_right ( ):

#*****************************************************************************80
#
## KERSHAW_EIGEN_RIGHT returns the right eigenvectors of the KERSHAW matrix.
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
#    Output, real X(4,4), the eigenvectors.
#
  import numpy as np

  x = np.array ( [ \
   [  0.500000000000000,  0.500000000000000,   \
     -0.548490135760211,  0.446271857698584 ], \
   [ -0.707106781186548, -0.000000000000000,   \
     -0.703402951241362, -0.072279237578588 ], \
   [  0.500000000000000, -0.500000000000000,   \
     -0.446271857698584, -0.548490135760211 ], \
   [ -0.000000000000000,  0.707106781186548,   \
      0.072279237578588, -0.703402951241362 ] ] )

  return x

def kershaw_eigenvalues ( ):

#*****************************************************************************80
#
## KERSHAW_EIGENVALUES returns the eigenvalues of the KERSHAW matrix.
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
#  Reference:
#
#    David Kershaw,
#    The Incomplete Cholesky-Conjugate Gradient Method for the Iterative
#    Solution of Systems of Linear Equations,
#    Journal of Computational Physics,
#    Volume 26, Number 1, January 1978, pages 43-65.
#
#  Parameters:
#
#    Output, real LAM(4), the eigenvalues of the matrix.
#
  import numpy as np

  lam = np.array ( [ \
    [ 5.828427124746192 ], \
    [ 5.828427124746188 ], \
    [ 0.171572875253810 ], \
    [ 0.171572875253810 ] ] )

  return lam

def kershaw_inverse ( ):

#*****************************************************************************80
#
## KERSHAW_INVERSE returns the inverse of the KERSHAW matrix.
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
#    Output, real A(4,4), the matrix.
#
  import numpy as np
#
#  Note that the matrix entries are listed by row.
#
  a = np.array ( [ \
    [  3.0,  2.0,  0.0, -2.0 ], \
    [  2.0,  3.0,  2.0,  0.0 ], \
    [  0.0,  2.0,  3.0,  2.0 ], \
    [ -2.0,  0.0,  2.0,  3.0 ] ] )

  return a

def kershaw_llt ( ):

#*****************************************************************************80
#
## KERSHAW_LLT returns the Cholesky factor of the KERSHAW matrix.
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

  a = np.array ( [ \
  [  1.732050807568877,  0.0,               \
     0.0,                0.0 ],             \
  [ -1.154700538379252,  1.290994448735805, \
     0.0,                0.0 ],             \
  [                0.0, -1.549193338482967, \
     0.774596669241483,  0.0 ],             \
  [  1.154700538379252,  1.032795558988645, \
    -0.516397779494321,  0.577350269189626 ] ] )

  return a

def kershaw_test ( ):

#*****************************************************************************80
#
## KERSHAW_TEST tests KERSHAW.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 February 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'KERSHAW_TEST'
  print '  KERSHAW computes the KERSHAW matrix.'

  n = 4
  a = kershaw ( )
  r8mat_print ( n, n, a, '  KERSHAW matrix:' )

  print ''
  print 'KERSHAW_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  kershaw_test ( )
  kershaw_condition_test ( )
  kershaw_determinant_test ( )
  timestamp ( )
