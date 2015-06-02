#! /usr/bin/env python
#
def daub4 ( n ):

#*****************************************************************************80
#
## DAUB4 returns the DAUB4 matrix.
#
#  Discussion:
#
#    The DAUB4 matrix is the Daubechies wavelet transformation matrix
#    with 4 coefficients.
#
#  Properties:
#
#    The family of matrices is nested as a function of N.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#    N must be at least 4 and a multiple of 2.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
  from math import sqrt
  from i4_wrap import i4_wrap
  from sys import exit

  if ( n < 4 or ( n % 2 ) != 0 ):
    print ''
    print 'DAUB4 - Fatal error!'
    print '  N must be at least 4 and a multiple of 2.'
    exit ( 'DAUB4 - Fatal error!' )

  a = np.zeros ( [ n, n ] )

  c0 = ( 1.0 + sqrt ( 3.0 ) ) / sqrt ( 32.0 )
  c1 = ( 3.0 + sqrt ( 3.0 ) ) / sqrt ( 32.0 )
  c2 = ( 3.0 - sqrt ( 3.0 ) ) / sqrt ( 32.0 )
  c3 = ( 1.0 - sqrt ( 3.0 ) ) / sqrt ( 32.0 )

  for i in range ( 0, n - 1, 2 ):
 
    a[i,i]                    =   c0
    a[i,i+1]                  =   c1
    a[i,i4_wrap(i+2,0,n-1)]   =   c2
    a[i,i4_wrap(i+3,0,n-1)]   =   c3

    a[i+1,i]                  =   c3
    a[i+1,i+1]                = - c2
    a[i+1,i4_wrap(i+2,0,n-1)] =   c1
    a[i+1,i4_wrap(i+3,0,n-1)] = - c0

  return a

def daub4_condition ( n ):

#*****************************************************************************80
#
## DAUB4_CONDITION returns the L1 condition of the DAUB4 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of the matrix.
#
#    Output, real VALUE, the condition.
#
  import numpy as np

  c0 = ( 1.0 + np.sqrt ( 3.0 ) ) / np.sqrt ( 32.0 )
  c1 = ( 3.0 + np.sqrt ( 3.0 ) ) / np.sqrt ( 32.0 )
  c2 = ( 3.0 - np.sqrt ( 3.0 ) ) / np.sqrt ( 32.0 )
  c3 = ( 1.0 - np.sqrt ( 3.0 ) ) / np.sqrt ( 32.0 )

  a_norm = np.abs ( c0 ) + np.abs ( c1 ) + np.abs ( c2 ) + np.abs ( c3 )
  b_norm = a_norm
  value = a_norm * b_norm

  return value

def daub4_condition_test ( ):

#*****************************************************************************80
#
## DAUB4_CONDITION_TEST tests DAUB4_CONDITION.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    25 January 2015
#
#  Author:
#
#    John Burkardt
#
  from daub4 import daub4
  from r8mat_print import r8mat_print

  print ''
  print 'DAUB4_CONDITION_TEST'
  print '  DAUB4_CONDITION computes the condition of the DAUB4 matrix.'

  m = 8
  n = m

  a = daub4 ( n )
  r8mat_print ( m, n, a, '  DAUB4 matrix:' )

  value = daub4_condition ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'DAUB4_CONDITION_TEST'
  print '  Normal end of execution.'

  return

def daub4_determinant ( n ):

#*****************************************************************************80
#
## DAUB4_DETERMINANT returns the determinant of the DAUB4 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the dimension of the matrix.
#
#    Output, real DETERM, the determinant.
#
  determ = - 1.0

  return determ

def daub4_determinant_test ( ):

#*****************************************************************************80
#
## DAUB4_DETERMINANT_TEST tests DAUB4_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 January 2015
#
#  Author:
#
#    John Burkardt
#
  from daub4 import daub4
  from r8mat_print import r8mat_print

  print ''
  print 'DAUB4_DETERMINANT_TEST'
  print '  DAUB4_DETERMINANT computes the determinant of the DAUB4 matrix.'

  m = 8
  n = m

  a = daub4 ( n )
  r8mat_print ( m, n, a, '  DAUB4 matrix:' )

  value = daub4_determinant ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'DAUB4_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def daub4_inverse ( n ):

#*****************************************************************************80
#
## DAUB4_INVERSE returns the inverse of the DAUB4 matrix.
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
#    Input, integer N, the order of the matrix.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np

  a = daub4 ( n )
  a = np.transpose ( a )

  return a

def daub4_test ( ):

#*****************************************************************************80
#
## DAUB4_TEST tests DAUB4.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    11 January 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'DAUB4_TEST'
  print '  DAUB4 computes the DAUB4 matrix.'

  m = 8
  n = m

  a = daub4 ( n )
  r8mat_print ( m, n, a, '  DAUB4 matrix:' )

  print ''
  print 'DAUB4_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  daub4_test ( )
  timestamp ( )
