#! /usr/bin/env python
#
def rutis5 ( ):

#*****************************************************************************80
#
## RUTIS5 returns the RUTIS5 matrix.
#
#  Example:
#
#    10  1  4  0
#    1  10  5 -1
#    4   5 10  7
#    0  -1  7  9
#
#  Properties:
#
#    A is symmetric: A' = A.
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
#    20 October 2007
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John Todd,
#    Basic Numerical Mathematics, Volume 2: Numerical Algebra,
#    Academic Press, 1977.
#
#  Parameters:
#
#    Output, real A(4,4), the matrix.
#
  import numpy as np

  a = np.array ( [ \
   [ 10.0,  1.0,  4.0,  0.0 ], \
   [  1.0, 10.0,  5.0, -1.0 ], \
   [  4.0,  5.0, 10.0,  7.0 ], \
   [  0.0, -1.0,  7.0,  9.0 ] ] );

  return a

def rutis5_condition ( ):

#*****************************************************************************80
#
## RUTIS5_CONDITION returns the L1 condition of the RUTIS5 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 December 2014
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real COND, the L1 condition number.
#
  cond = 62608.0

  return cond

def rutis5_condition_test ( ):

#*****************************************************************************80
#
## RUTIS5_CONDITION_TEST tests RUTIS5_CONDITION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 December 2014
#
#  Author:
#
#    John Burkardt
#
  from rutis5 import rutis5
  from r8mat_print import r8mat_print

  print ''
  print 'RUTIS5_CONDITION_TEST'
  print '  RUTIS5_CONDITION computes the condition of the RUTIS5 matrix.'
  print ''

  seed = 123456789

  n = 4
  a = rutis5 ( )
  r8mat_print ( n, n, a, '  RUTIS5 matrix:' )

  value = rutis5_condition ( )
  print ''
  print '  Value =  %' % ( value )

  print ''
  print 'RUTIS5_CONDITION_TEST'
  print '  Normal end of execution.'

  return

def rutis5_determinant ( ):

#*****************************************************************************80
#
## RUTIS5_DETERMINANT returns the determinant of the RUTIS5 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 January 2015
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

def rutis5_determinant_test ( ):

#*****************************************************************************80
#
## RUTIS5_DETERMINANT_TEST tests RUTIS5_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    23 January 2015
#
#  Author:
#
#    John Burkardt
#
  from rutis5 import rutis5
  from r8mat_print import r8mat_print

  print ''
  print 'RUTIS5_DETERMINANT_TEST'
  print '  RUTIS5_DETERMINANT computes the determinant of the RUTIS5 matrix.'
  print ''

  seed = 123456789

  n = 4
  a = rutis1 ( )
  r8mat_print ( n, n, a, '  RUTIS5 matrix:' )

  value = rutis5_determinant ( )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'RUTIS5_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def rutis5_eigen_right ( ):

#*****************************************************************************80
#
## RUTIS5_EIGEN_RIGHT returns the right eigenvectors of the RUTIS5 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
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

  a = np.array ( [ \
   [  0.356841883715928, \
      0.382460905084129, \
      0.718205429169617, \
      0.458877421126365 ], \
   [ -0.341449101169948, \
     -0.651660990948502, \
      0.087555987078632, \
      0.671628180850787 ], \
   [  0.836677864423576, \
     -0.535714651223808, \
     -0.076460316709461, \
     -0.084461728708607 ], \
   [ -0.236741488801405, \
     -0.376923628103094, \
      0.686053008598214, \
    - 0.575511351279045 ] ] )

  a = np.transpose ( a )
  
  return a

def rutis5_eigenvalues ( ):

#*****************************************************************************80
#
## RUTIS5_EIGENVALUES returns the eigenvalues of the RUTIS5 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real LAM(4), the eigenvalues.
#
  import numpy as np

  lam = np.array ( [ \
    [ 19.122479087555860 ], \
    [ 10.882816916492464 ], \
    [  8.994169735037230 ], \
    [  0.000534260914449 ] ] )

  return lam

def rutis5_inverse ( ):

#*****************************************************************************80
#
## RUTIS5_INVERSE returns the inverse of the RUTIS5 matrix.
#
#  Example:
#
#     105  167 -304  255
#     167  266 -484  406
#    -304 -484  881 -739
#     255  406 -739  620
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    17 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    John Todd,
#    Basic Numerical Mathematics, Volume 2: Numerical Algebra,
#    Academic Press, 1977.
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
    [  105.0,  167.0, -304.0,  255.0 ], \
    [  167.0,  266.0, -484.0,  406.0 ], \
    [ -304.0, -484.0,  881.0, -739.0 ], \
    [  255.0,  406.0, -739.0,  620.0 ] ] )

  return a

def rutis5_test ( ):

#*****************************************************************************80
#
## RUTIS5_TEST tests RUTIS5.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 December 2014
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'RUTIS5_TEST'
  print '  RUTIS5 computes the RUTIS5 matrix.'

  n = 4
  a = rutis5 ( )
  r8mat_print ( n, n, a, '  RUTIS5 matrix:' )

  print ''
  print 'RUTIS5_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  rutis5_test ( )
  timestamp ( )
