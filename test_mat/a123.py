#! /usr/bin/env python
#
def a123 ( ):

#*****************************************************************************80
#
## A123 returns the A123 matrix.
#
#  Example:
#
#    1 2 3
#    4 5 6
#    7 8 9
#
#  Properties:
#
#    A is integral.
#
#    A is not symmetric.
#
#    A is singular.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real A(3,3), the matrix.
#
  import numpy as np

  a = np.zeros ( ( 3, 3 ) )

  k = 0
  for i in range ( 0, 3 ):
    for j in range ( 0, 3 ):
      k = k + 1
      a[i,j] = float ( k )

  return a

def a123_determinant ( ):

#*****************************************************************************80
#
## A123_DETERMINANT computes the determinant of the A123 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real VALUE, the determinant.
#
  value = 0.0

  return value

def a123_determinant_test ( ):

#*****************************************************************************80
#
## A123_DETERMINANT_TEST tests A123_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 March 2015
#
#  Author:
#
#    John Burkardt
#
  from a123 import a123
  from r8mat_print import r8mat_print

  print ''
  print 'A123_DETERMINANT_TEST'
  print '  A123_DETERMINANT computes the A123 determinant.'

  m = 3
  n = 3
  a = a123 ( )
  r8mat_print ( n, n, a, '  A123 matrix:' )

  value = a123_determinant ( )
  print '  Value =  %g' % ( value )

  print ''
  print 'A123_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def a123_eigen_left ( ):

#*****************************************************************************80
#
## A123_EIGEN_LEFT returns the left eigenvectors of the A123 matrix.
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
#    Output, real A(3,3), the eigenvectors.
#
  import numpy as np

  a = np.array ( [ \
    [ -0.464547273387671, -0.570795531228578, -0.677043789069485 ], \
    [ -0.882905959653586, -0.239520420054206,  0.403865119545174 ], \
    [  0.408248290463862, -0.816496580927726,  0.408248290463863 ] ] )

  return a

def a123_eigen_right ( ):

#*****************************************************************************80
#
## A123_EIGEN_RIGHT returns the right eigenvectors of the A123 matrix.
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
#    Output, real A(3,3), the right eigenvector matrix.
#
  import numpy as np

  a = np.array ( [ \
    [ -0.231970687246286,  -0.785830238742067,   0.408248290463864 ], \
    [ -0.525322093301234,  -0.086751339256628,  -0.816496580927726 ], \
    [ -0.818673499356181,   0.612327560228810,   0.408248290463863 ] ] )

  return a

def a123_eigenvalues ( ):

#*****************************************************************************80
#
## A123_EIGENVALUES returns the eigenvalues of the A123 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real LAM(3), the eigenvalues.
#
  import numpy as np

  lam = np.array ( [ \
   [ 16.116843969807043 ], \
   [ -1.116843969807043 ], \
   [  0.0 ] ] )

  return lam

def a123_null_left ( ):

#*****************************************************************************80
#
## A123_NULL_LEFT returns a left null vector for the A123 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real X(3), a left null vector.
#
  import numpy as np

  x = np.array ( [ [ 1.0 ], [ -2.0 ], [ 1.0 ] ] )

  return x

def a123_null_right ( ):

#*****************************************************************************80
#
## A123_NULL_RIGHT returns a right null vector for the A123 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real X(3), a right null vector.
#
  import numpy as np

  x = np.array ( [ [ 1.0 ], [ -2.0 ], [ 1.0 ] ] )

  return x

def a123_rhs ( ):

#*****************************************************************************80
#
## A123_RHS returns the A123 right hand side.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real B(3), the right hand side vector.
#
  import numpy as np

  b = np.array ( [ [ 10.0 ], [ 28.0 ], [ 46.0 ] ] )

  return b

def a123_solution ( ):

#*****************************************************************************80
#
## A123_SOLUTION returns the A123_SOLUTION
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real X(3), the solution.
#
  import numpy as np

  x = np.array ( [ [ 3.0 ], [ 2.0 ], [ 1.0 ] ] )

  return x

def a123_test ( ):

#*****************************************************************************80
#
## A123_TEST tests A123.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    10 March 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'A123_TEST'
  print '  A123 computes the A123 matrix.'

  n = 3
  a = a123 ( )
  r8mat_print ( n, n, a, '  A123 matrix:' )

  print ''
  print 'A123_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  a123_test ( )
  timestamp ( )
