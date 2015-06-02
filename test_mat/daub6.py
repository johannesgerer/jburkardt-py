#! /usr/bin/env python
#
def daub6 ( n ):

#*****************************************************************************80
#
## DAUB6 returns the DAUB6 matrix.
#
#  Discussion:
#
#    The DAUB6 matrix is the Daubechies wavelet transformation matrix
#    with 6 coefficients.
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
#    N must be at least 6 and a multiple of 2.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
  from math import sqrt
  from i4_wrap import i4_wrap
  from sys import exit

  if ( n < 6 or ( n % 2 ) != 0 ):
    print ''
    print 'DAUB6 - Fatal error!'
    print '  N must be at least 6 and a multiple of 2.'
    exit ( 'DAUB6 - Fatal error!' )

  a = np.zeros ( [ n, n ] )

  c0 =  1.0 + sqrt ( 10.0 ) +       sqrt ( 5.0 + sqrt ( 40.0 ) )
  c1 =  5.0 + sqrt ( 10.0 ) + 3.0 * sqrt ( 5.0 + sqrt ( 40.0 ) )
  c2 = 10.0 - sqrt ( 40.0 ) + 2.0 * sqrt ( 5.0 + sqrt ( 40.0 ) )
  c3 = 10.0 - sqrt ( 40.0 ) - 2.0 * sqrt ( 5.0 + sqrt ( 40.0 ) )
  c4 =  5.0 + sqrt ( 10.0 ) - 3.0 * sqrt ( 5.0 + sqrt ( 40.0 ) )
  c5 =  1.0 + sqrt ( 10.0 ) -       sqrt ( 5.0 + sqrt ( 40.0 ) )

  c0 = c0 / sqrt ( 512.0 )
  c1 = c1 / sqrt ( 512.0 )
  c2 = c2 / sqrt ( 512.0 )
  c3 = c3 / sqrt ( 512.0 )
  c4 = c4 / sqrt ( 512.0 )
  c5 = c5 / sqrt ( 512.0 )

  for i in range ( 0, n - 1, 2 ):
 
    a[i,i]                    =   c0
    a[i,i+1]                  =   c1
    a[i,i4_wrap(i+2,0,n-1)]   =   c2
    a[i,i4_wrap(i+3,0,n-1)]   =   c3
    a[i,i4_wrap(i+4,0,n-1)]   =   c4
    a[i,i4_wrap(i+5,0,n-1)]   =   c5

    a[i+1,i]                  =   c5
    a[i+1,i+1]                = - c4
    a[i+1,i4_wrap(i+2,0,n-1)] =   c3
    a[i+1,i4_wrap(i+3,0,n-1)] = - c2
    a[i+1,i4_wrap(i+4,0,n-1)] =   c1
    a[i+1,i4_wrap(i+5,0,n-1)] = - c0

  return a

def daub6_condition ( n ):

#*****************************************************************************80
#
## DAUB6_CONDITION returns the L1 condition of the DAUB6 matrix.
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

  c0 =  1.0 + np.sqrt ( 10.0 ) +         np.sqrt ( 5.0 + np.sqrt ( 40.0 ) )
  c1 =  5.0 + np.sqrt ( 10.0 ) +   3.0 * np.sqrt ( 5.0 + np.sqrt ( 40.0 ) )
  c2 = 10.0 - np.sqrt ( 40.0 ) +   2.0 * np.sqrt ( 5.0 + np.sqrt ( 40.0 ) )
  c3 = 10.0 - np.sqrt ( 40.0 ) -   2.0 * np.sqrt ( 5.0 + np.sqrt ( 40.0 ) )
  c4 =  5.0 + np.sqrt ( 10.0 ) -   3.0 * np.sqrt ( 5.0 + np.sqrt ( 40.0 ) )
  c5 =  1.0 + np.sqrt ( 10.0 ) -         np.sqrt ( 5.0 + np.sqrt ( 40.0 ) )

  c0 = c0 / np.sqrt ( 512.0 )
  c1 = c1 / np.sqrt ( 512.0 )
  c2 = c2 / np.sqrt ( 512.0 )
  c3 = c3 / np.sqrt ( 512.0 )
  c4 = c4 / np.sqrt ( 512.0 )
  c5 = c5 / np.sqrt ( 512.0 )

  a_norm = np.abs ( c0 ) + np.abs ( c1 ) \
         + np.abs ( c2 ) + np.abs ( c3 ) \
         + np.abs ( c4 ) + np.abs ( c5 )
  b_norm = a_norm
  value = a_norm * b_norm

  return value

def daub6_condition_test ( ):

#*****************************************************************************80
#
## DAUB6_CONDITION_TEST tests DAUB6_CONDITION.
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
  from daub6 import daub6
  from r8mat_print import r8mat_print

  print ''
  print 'DAUB6_CONDITION_TEST'
  print '  DAUB6_CONDITION computes the condition of the DAUB6 matrix.'

  m = 12
  n = m

  a = daub6 ( n )
  r8mat_print ( m, n, a, '  DAUB6 matrix:' )

  value = daub6_condition ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'DAUB6_CONDITION_TEST'
  print '  Normal end of execution.'

  return

def daub6_determinant ( n ):

#*****************************************************************************80
#
## DAUB6_DETERMINANT returns the determinant of the DAUB6 matrix.
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
  determ = + 1.0

  return determ

def daub6_determinant_test ( ):

#*****************************************************************************80
#
## DAUB6_DETERMINANT_TEST tests DAUB6_DETERMINANT.
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
  from daub6 import daub6
  from r8mat_print import r8mat_print

  print ''
  print 'DAUB6_DETERMINANT_TEST'
  print '  DAUB6_DETERMINANT computes the determinant of the DAUB6 matrix.'

  m = 12
  n = m

  a = daub6 ( n )
  r8mat_print ( m, n, a, '  DAUB6 matrix:' )

  value = daub6_determinant ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'DAUB6_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def daub6_inverse ( n ):

#*****************************************************************************80
#
## DAUB6_INVERSE returns the inverse of the DAUB6 matrix.
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

  a = daub6 ( n )
  a = np.transpose ( a )

  return a

def daub6_test ( ):

#*****************************************************************************80
#
## DAUB6_TEST tests DAUB6.
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
  print 'DAUB6_TEST'
  print '  DAUB6 computes the DAUB6 matrix.'

  m = 12
  n = m

  a = daub6 ( n )
  r8mat_print ( m, n, a, '  DAUB6 matrix:' )

  print ''
  print 'DAUB6_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  daub6_test ( )
  timestamp ( )
