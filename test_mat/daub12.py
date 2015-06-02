#! /usr/bin/env python
#
def daub12 ( n ):

#*****************************************************************************80
#
## DAUB12 returns the DAUB12 matrix.
#
#  Discussion:
#
#    The DAUB12 matrix is the Daubechies wavelet transformation matrix
#    with 12 coefficients.
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
#    16 January 2015
#
#  Author:
#
#    John Burkardt
#
#  Parameters:
#
#    Input, integer N, the order of the matrix.
#    N must be at least 12 and a multiple of 2.
#
#    Output, real A(N,N), the matrix.
#
  import numpy as np
  from math import sqrt
  from i4_wrap import i4_wrap
  from sys import exit

  if ( n < 12 or ( n % 2 ) != 0 ):
    print ''
    print 'DAUB12 - Fatal error!'
    print '  N must be at least 12 and a multiple of 2.'
    exit ( 'DAUB12 - Fatal error!' )

  a = np.zeros ( [ n, n ] )

  c = np.array ( [ \
    0.1115407433501095, \
    0.4946238903984533, \
    0.7511339080210959, \
    0.3152503517091982, \
   -0.2262646939654400, \
   -0.1297668675672625, \
    0.0975016055873225, \
    0.0275228655303053, \
   -0.0315820393174862, \
    0.0005538422011614, \
    0.0047772575109455, \
   -0.0010773010853085 ] )

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
    a[i,i4_wrap(i+10,0,n-1)]  =   c[10]
    a[i,i4_wrap(i+11,0,n-1)]  =   c[11]

    a[i+1,i]                   =   c[11]
    a[i+1,i+1]                 = - c[10]
    a[i+1,i4_wrap(i+2,0,n-1)]  =   c[9]
    a[i+1,i4_wrap(i+3,0,n-1)]  = - c[8]
    a[i+1,i4_wrap(i+4,0,n-1)]  =   c[7]
    a[i+1,i4_wrap(i+5,0,n-1)]  = - c[6]
    a[i+1,i4_wrap(i+6,0,n-1)]  =   c[5]
    a[i+1,i4_wrap(i+7,0,n-1)]  = - c[4]
    a[i+1,i4_wrap(i+8,0,n-1)]  =   c[3]
    a[i+1,i4_wrap(i+9,0,n-1)]  = - c[2]
    a[i+1,i4_wrap(i+10,0,n-1)] =   c[1]
    a[i+1,i4_wrap(i+11,0,n-1)] = - c[0]

  return a

def daub12_condition ( n ):

#*****************************************************************************80
#
## DAUB12_CONDITION returns the L1 condition of the DAUB12 matrix.
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
    0.1115407433501095, \
    0.4946238903984533, \
    0.7511339080210959, \
    0.3152503517091982, \
   -0.2262646939654400, \
   -0.1297668675672625, \
    0.0975016055873225, \
    0.0275228655303053, \
   -0.0315820393174862, \
    0.0005538422011614, \
    0.0047772575109455, \
   -0.0010773010853085 ] )

  a_norm = np.sum ( np.abs ( c ) )
  b_norm = a_norm
  value = a_norm * b_norm

  return value

def daub12_condition_test ( ):

#*****************************************************************************80
#
## DAUB12_CONDITION_TEST tests DAUB12_CONDITION.
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
  from daub12 import daub12
  from r8mat_print import r8mat_print

  print ''
  print 'DAUB12_CONDITION_TEST'
  print '  DAUB12_CONDITION computes the condition of the DAUB12 matrix.'

  m = 24
  n = m

  a = daub12 ( n )
  r8mat_print ( m, n, a, '  DAUB12 matrix:' )

  value = daub12_condition ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'DAUB12_CONDITION_TEST'
  print '  Normal end of execution.'

  return

def daub12_determinant ( n ):

#*****************************************************************************80
#
## DAUB12_DETERMINANT returns the determinant of the DAUB12 matrix.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 January 2015
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

def daub12_determinant_test ( ):

#*****************************************************************************80
#
## DAUB12_DETERMINANT_TEST tests DAUB12_DETERMINANT.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 January 2015
#
#  Author:
#
#    John Burkardt
#
  from daub12 import daub12
  from r8mat_print import r8mat_print

  print ''
  print 'DAUB12_DETERMINANT_TEST'
  print '  DAUB12_DETERMINANT computes the determinant of the DAUB12 matrix.'

  m = 24
  n = m

  a = daub12 ( n )
  r8mat_print ( m, n, a, '  DAUB12 matrix:' )

  value = daub12_determinant ( n )

  print ''
  print '  Value =  %g' % ( value )

  print ''
  print 'DAUB12_DETERMINANT_TEST'
  print '  Normal end of execution.'

  return

def daub12_inverse ( n ):

#*****************************************************************************80
#
## DAUB12_INVERSE returns the inverse of the DAUB12 matrix.
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

  a = daub12 ( n )
  a = np.transpose ( a )

  return a

def daub12_test ( ):

#*****************************************************************************80
#
## DAUB12_TEST tests DAUB12.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    16 January 2015
#
#  Author:
#
#    John Burkardt
#
  from r8mat_print import r8mat_print

  print ''
  print 'DAUB12_TEST'
  print '  DAUB12 computes the DAUB12 matrix.'

  m = 24
  n = m

  a = daub12 ( n )
  r8mat_print ( m, n, a, '  DAUB12 matrix:' )

  print ''
  print 'DAUB12_TEST'
  print '  Normal end of execution.'

  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  daub12_test ( )
  timestamp ( )
