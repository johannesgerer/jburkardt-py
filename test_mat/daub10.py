#! /usr/bin/env python
#
def daub10 ( n ):

#*****************************************************************************80
#
## DAUB10 returns the DAUB10 matrix.
#
#  Discussion:
#
#    The DAUB10 matrix is the Daubechies wavelet transformation matrix
#    with 10 coefficients.
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
#    14 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#    N must be at least 10 and a multiple of 2.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
  from math import sqrt
  from i4_wrap import i4_wrap
  from sys import exit

  if ( n < 10 or ( n % 2 ) != 0 ):
    print ''
    print 'DAUB10 - Fatal error!'
    print '  N must be at least 10 and a multiple of 2.'
    exit ( 'DAUB10 - Fatal error!' )

  a = np.zeros ( [ n, n ] )

  c = np.array ( [ \
    0.1601023979741929, \
    0.6038292697971895, \
    0.7243085284377726, \
    0.1384281459013203, \
   -0.2422948870663823, \
   -0.0322448695846381, \
    0.0775714938400459, \
   -0.0062414902127983, \
   -0.0125807519990820, \
    0.0033357252854738 ] )

  for i in range ( 0, n - 1, 2 ):
 
    a[i,i]                    =   c[0]
    a[i,i+1]                  =   c[1]
    a[i,i4_wrap(i+2,0,n-1)]   =   c[2]
    a[i,i4_wrap(i+3,0,n-1)]   =   c[3]
    a[i,i4_wrap(i+4,0,n-1)]   =   c[4]
    a[i,i4_wrap(i+5,0,n-1)]   =   c[5]
    a[i,i4_wrap(i+6,0,n-1)]   =   c[6]
    a[i,i4_wrap(i+7,0,n-1)]   =   c[7]
    a[i,i4_wrap(i+8,0,n-1)]   =   c[8]
    a[i,i4_wrap(i+9,0,n-1)]   =   c[9]

    a[i+1,i]                  =   c[9]
    a[i+1,i+1]                = - c[8]
    a[i+1,i4_wrap(i+2,0,n-1)] =   c[7]
    a[i+1,i4_wrap(i+3,0,n-1)] = - c[6]
    a[i+1,i4_wrap(i+4,0,n-1)] =   c[5]
    a[i+1,i4_wrap(i+5,0,n-1)] = - c[4]
    a[i+1,i4_wrap(i+6,0,n-1)] =   c[3]
    a[i+1,i4_wrap(i+7,0,n-1)] = - c[2]
    a[i+1,i4_wrap(i+8,0,n-1)] =   c[1]
    a[i+1,i4_wrap(i+9,0,n-1)] = - c[0]

  return a

def daub10_condition ( n ):

#*****************************************************************************80
#
## DAUB10_CONDITION returns the L1 condition of the DAUB10 matrix.
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
    0.1601023979741929, \
    0.6038292697971895, \
    0.7243085284377726, \
    0.1384281459013203, \
   -0.2422948870663823, \
   -0.0322448695846381, \
    0.0775714938400459, \
   -0.0062414902127983, \
   -0.0125807519990820, \
    0.0033357252854738 ] )

  a_norm = np.sum ( np.abs ( c ) )
  b_norm = a_norm
  value = a_norm * b_norm

  return value

def daub10_condition_test ( ):

#*****************************************************************************80
#
## DAUB10_CONDITION_TEST tests DAUB10_CONDITION.
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
  from daub10 import daub10
  from r8mat_print import r8mat_print

  print ''
  print 'DAUB10_CONDITION_TEST'
  print '  DAUB10_CONDITION computes the condition of the DAUB10 matrix.'

  m = 20
  n = m

  a = daub10 ( n )
  r8mat_print ( m, n, a, '  DAUB10 matrix:' )

  value = daub10_condition ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'DAUB10_CONDITION_TEST'
  print '  Normal end of execution.'

  return

def daub10_determinant ( n ):

#*****************************************************************************80
#
## DAUB10_DETERMINANT returns the determinant of the DAUB10 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 January 2015
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

def daub10_determinant_test ( ):

#*****************************************************************************80
#
## DAUB10_DETERMINANT_TEST tests DAUB10_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 January 2015
#
#  Author:
#
#    John Burkardt
#
  from daub10 import daub10
  from r8mat_print import r8mat_print

  print ''
  print 'DAUB10_DETERMINANT_TEST'
  print '  DAUB10_DETERMINANT computes the determinant of the DAUB10 matrix.'

  m = 20
  n = m

  a = daub10 ( n )
  r8mat_print ( m, n, a, '  DAUB10 matrix:' )

  value = daub10_determinant ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'DAUB10_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def daub10_inverse ( n ):

#*****************************************************************************80
#
## DAUB10_INVERSE returns the inverse of the DAUB10 matrix.
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

  a = daub10 ( n )
  a = np.transpose ( a )

  return a

def daub10_test ( ):

#*****************************************************************************80
#
## DAUB10_TEST tests DAUB10.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    14 January 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'DAUB10_TEST'
  print '  DAUB10 computes the DAUB10 matrix.'

  m = 20
  n = m

  a = daub10 ( n )
  r8mat_print ( m, n, a, '  DAUB10 matrix:' )

  print ''
  print 'DAUB10_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  daub10_test ( )
  timestamp ( )
