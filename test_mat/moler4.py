#! /usr/bin/env python
#
def moler4 ( ):

#*****************************************************************************80
#
## MOLER4 returns the MOLER4 matrix.
#
#  Example:
#
#    0  2  0 -1
#    1  0  0  0
#    0  1  0  0
#    0  0  1  0
#
#  Properties:
#
#    A is integral, therefore det ( A ) is integral, and 
#    det ( A ) * inverse ( A ) is integral.
#
#    A is the companion matrix of the polynomial X^4-2X^2+1=0.
#
#    A has eigenvalues -1, -1, +1, +1.
#
#    A can cause problems to a standard QR algorithm, which
#    can fail to converge.
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
#    Output, real A(4,4), the matrix.
#
  import numpy as np

  a = np.array ( [ \
    [ 0.0,  2.0,  0.0, -1.0 ], \
    [ 1.0,  0.0,  0.0,  0.0 ], \
    [ 0.0,  1.0,  0.0,  0.0 ], \
    [ 0.0,  0.0,  1.0,  0.0 ] ] )

  return a

def moler4_determinant ( ):

#*****************************************************************************80
#
## MOLER4_DETERMINANT returns the determinant of the MOLER4 matrix.
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
#    Output, real VALUE, the determinant.
#
  value = 1.0

  return value

def moler4_determinant_test ( ):

#*****************************************************************************80
#
## MOLER4_DETERMINANT_TEST tests MOLER4_DETERMINANT.
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
  from moler4 import moler3
  from r8mat_print import r8mat_print
 
  print ''
  print 'MOLER4_DETERMINANT_TEST'
  print '  MOLER4_DETERMINANT computes the determinant of the MOLER4 matrix.'
  print ''

  m = 4
  n = m

  a = moler4 ( )
  r8mat_print ( m, n, a, '  MOLER4 matrix:' )

  value = moler4_determinant ( )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'MOLER4_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def moler4_test ( ):

#*****************************************************************************80
#
## MOLER4_TEST tests MOLER4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    26 January 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'MOLER4_TEST'
  print '  MOLER4 computes the MOLER4 matrix.'

  m = 4
  n = m

  a = moler4 ( )
  r8mat_print ( m, n, a, '  MOLER4 matrix:' )

  print ''
  print 'MOLER4_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  moler4_test ( )
  timestamp ( )
