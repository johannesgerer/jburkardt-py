#! /usr/bin/env python
#
def daub8 ( n ):

#*****************************************************************************80
#
## DAUB8 returns the DAUB8 matrix.
#
#  Discussion:
#
#    The DAUB8 matrix is the Daubechies wavelet transformation matrix
#    with 8 coefficients.
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
#    12 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#    N must be at least 8 and a multiple of 2.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
  from math import sqrt
  from i4_wrap import i4_wrap
  from sys import exit

  if ( n < 8 or ( n % 2 ) != 0 ):
    print ''
    print 'DAUB8 - Fatal error!'
    print '  N must be at least 8 and a multiple of 2.'
    exit ( 'DAUB8 - Fatal error!' )

  a = np.zeros ( [ n, n ] )

  c0 =   0.2303778133088964
  c1 =   0.7148465705529154
  c2 =   0.6308807679298587
  c3 =  -0.0279837694168599
  c4 =  -0.1870348117190931
  c5 =   0.0308413818355607
  c6 =   0.0328830116668852
  c7 =  -0.0105974017850690

  for i in range ( 0, n - 1, 2 ):
 
    a[i,i]                    =   c0
    a[i,i+1]                  =   c1
    a[i,i4_wrap(i+2,0,n-1)]   =   c2
    a[i,i4_wrap(i+3,0,n-1)]   =   c3
    a[i,i4_wrap(i+4,0,n-1)]   =   c4
    a[i,i4_wrap(i+5,0,n-1)]   =   c5
    a[i,i4_wrap(i+6,0,n-1)]   =   c6
    a[i,i4_wrap(i+7,0,n-1)]   =   c7

    a[i+1,i]                  =   c7
    a[i+1,i+1]                = - c6
    a[i+1,i4_wrap(i+2,0,n-1)] =   c5
    a[i+1,i4_wrap(i+3,0,n-1)] = - c4
    a[i+1,i4_wrap(i+4,0,n-1)] =   c3
    a[i+1,i4_wrap(i+5,0,n-1)] = - c2
    a[i+1,i4_wrap(i+6,0,n-1)] =   c1
    a[i+1,i4_wrap(i+7,0,n-1)] = - c0

  return a

def daub8_condition ( n ):

#*****************************************************************************80
#
## DAUB8_CONDITION returns the L1 condition of the DAUB8 matrix.
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

  c = np.array ( [ \
    0.2303778133088964, \
    0.7148465705529154, \
    0.6308807679298587, \
   -0.0279837694168599, \
   -0.1870348117190931, \
    0.0308413818355607, \
    0.0328830116668852, \
   -0.0105974017850690 ] )

  a_norm = np.sum ( np.abs ( c ) )
  b_norm = a_norm
  value = a_norm * b_norm

  return value

def daub8_condition_test ( ):

#*****************************************************************************80
#
## DAUB8_CONDITION_TEST tests DAUB8_CONDITION.
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
  from daub8 import daub8
  from r8mat_print import r8mat_print

  print ''
  print 'DAUB8_CONDITION_TEST'
  print '  DAUB8_CONDITION computes the condition of the DAUB8 matrix.'

  m = 16
  n = m

  a = daub8 ( n )
  r8mat_print ( m, n, a, '  DAUB8 matrix:' )

  value = daub8_condition ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'DAUB8_CONDITION_TEST'
  print '  Normal end of execution.'

  return

def daub8_determinant ( n ):

#*****************************************************************************80
#
## DAUB8_DETERMINANT returns the determinant of the DAUB8 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 January 2015
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

def daub8_determinant_test ( ):

#*****************************************************************************80
#
## DAUB8_DETERMINANT_TEST tests DAUB8_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 January 2015
#
#  Author:
#
#    John Burkardt
#
  from daub8 import daub8
  from r8mat_print import r8mat_print

  print ''
  print 'DAUB8_DETERMINANT_TEST'
  print '  DAUB8_DETERMINANT computes the determinant of the DAUB8 matrix.'

  m = 16
  n = m

  a = daub8 ( n )
  r8mat_print ( m, n, a, '  DAUB8 matrix:' )

  value = daub8_determinant ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'DAUB8_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def daub8_inverse ( n ):

#*****************************************************************************80
#
## DAUB8_INVERSE returns the inverse of the DAUB8 matrix.
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

  a = daub8 ( n )
  a = np.transpose ( a )

  return a

def daub8_test ( ):

#*****************************************************************************80
#
## DAUB8_TEST tests DAUB8.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    12 January 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'DAUB8_TEST'
  print '  DAUB8 computes the DAUB8 matrix.'

  m = 16
  n = m

  a = daub8 ( n )
  r8mat_print ( m, n, a, '  DAUB8 matrix:' )

  print ''
  print 'DAUB8_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  daub8_test ( )
  timestamp ( )
