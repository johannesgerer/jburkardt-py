#! /usr/bin/env python
#
def complex_i ( ):

#*****************************************************************************80
#
## COMPLEX_I returns the COMPLEX_I matrix.
#
#  Discussion:
#
#    This is a 2 by 2 matrix that behaves like the imaginary unit.
#
#  Formula:
#
#    0 1
#   -1 0
#
#  Properties:
#
#    A is integral: int ( A ) = A.
#
#    A is anti-involutional: A * A = - I
#
#    A * A * A * A = I
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real A(2,2), the matrix.
#
  import numpy as np

  a = np.array ( [
    [  0.0, 1.0 ], \
    [ -1.0, 0.0 ] \
  ] )

  return a

def complex_i_determinant ( ):

#*****************************************************************************80
#
## COMPLEX_I_DETERMINANT returns the determinant of the COMPLEX_I matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real DETERM, the determinant.
#
  determ = 1.0

  return determ

def complex_i_determinant_test ( ):

#*****************************************************************************80
#
## COMPLEX_I_DETERMINANT_TEST tests COMPLEX_I_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
  from complex_i import complex_i
  from r8mat_print import r8mat_print

  print ''
  print 'COMPLEX_I_DETERMINANT_TEST'
  print '  COMPLEX_I_DETERMINANT computes the determinant of the COMPLEX_I matrix.'

  m = 2
  n = m

  a = complex_i ( )
  r8mat_print ( m, n, a, '  COMPLEX_I matrix:' )

  value = complex_i_determinant ( )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'COMPLEX_I_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def complex_i_inverse ( ):

#*****************************************************************************80
#
## COMPLEX_I_INVERSE returns the inverse of the COMPLEX_I matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 March 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Output, real A(2,2), the matrix.
#
  import numpy as np

  a = np.array ( [ \
    [  0.0, -1.0 ], \
    [ +1.0,  0.0 ] ] )

  return a

def complex_i_test ( ):

#*****************************************************************************80
#
## COMPLEX_I_TEST tests COMPLEX_I.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    09 January 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'COMPLEX_I_TEST'
  print '  COMPLEX_I computes the COMPLEX_I matrix.'

  m = 2
  n = m

  a = complex_i ( )
  r8mat_print ( m, n, a, '  COMPLEX_I matrix:' )

  print ''
  print 'COMPLEX_I_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  complex_i_test ( )
  timestamp ( )
